#!/usr/bin/env python3

import re
import os
import sys
import hmac
import json
import hashlib
import secrets
import getpass
import binascii
import unicodedata
from typing import Union
from typing import Sequence
from Crypto.Cipher import AES
from argparse import ArgumentParser, Namespace


##############################################################################################################################
#  These are our crypto and related functions - adapted from classroom content 
##############################################################################################################################

def mac_term(word: str, key: bytes):
    # This method should MAC the given word/terms
    return hmac.new(key, word.encode(), hashlib.sha256).hexdigest()

def encrypt_file_data(data: bytes, base_key: bytes, nonce: bytes):
    # All steps to encrypt, and mac, given we do KDF key schedule
    _k0, _k1, _k2, _k3, _k4, k5, _k6 = kdf(base_key, nonce)  # we'll need keys 1-4 here for feistel and 5, the mac
    ciphertext = four_pass_ENCRYPT(base_key, data, nonce)
    # Make use of HMAC-SHA2-256 and the MAC key to MAC the ciphertext. This will allow determination of tampering
    # without having to do decrypt operation.
    macd = hmac.new(k5, ciphertext, hashlib.sha256).digest()
    return macd, ciphertext


def decrypt_file_data(data: bytes, base_key: bytes, nonce: bytes):
    # All steps to deccrypt, given we do have KDF key schedule
    return four_pass_DECRYPT(base_key, data, nonce)


def _xor_bytes(bytes1: bytes, bytes2: bytes):
    return bytes([x ^ y for x, y in zip(bytes1, bytes2)])


# Increment a 16 byte value as per amount - this is used in nonce increment and key schedule. Not used independently.
def _increment(valuetoincrement: Union[bytes, str], amount: int):
    # we use this to increment the 16byt nonce values by 1, and be able to handle overflow on FFs
    try:
        if isinstance(valuetoincrement, str):
            valuetoincrement = valuetoincrement.encode()
        incremented = (int.from_bytes(valuetoincrement, 'big') + amount).to_bytes(16, "big")
    except OverflowError:
        # value won't fit into the payload, wrap round to 0
        incremented = ((int.from_bytes(valuetoincrement, 'big') + amount) % 256).to_bytes(16, "big")
    return incremented


# Block encryption handling for 16 byte blocks. Not used independently.
#
def _one_ctr_block(key: bytes, nonce_plus_ctr: bytes):
    ctx = AES.new(key, mode=AES.MODE_ECB)
    return ctx.encrypt(nonce_plus_ctr)


# Key Schedule Generation. Takes base key, which is the left 16 bytes of the master key and the nonce,
# which is the right 16 bytes of master key. It increments and creates 7 keys, stored in list. Key
# schedule will be used in encryption and decryption.
#
def kdf(base_key: bytes, nonce_: bytes):
    # We take base key, add nothing to first, increment by 1 for each key 1-6
    result = (
        _one_ctr_block(base_key, nonce_),
        _one_ctr_block(base_key, _increment(nonce_, 1)),
        _one_ctr_block(base_key, _increment(nonce_, 2)),
        _one_ctr_block(base_key, _increment(nonce_, 3)),
        _one_ctr_block(base_key, _increment(nonce_, 4)),
        _one_ctr_block(base_key, _increment(nonce_, 5)),
        _one_ctr_block(base_key, _increment(nonce_, 6)),
    )
    return result


# AES Single Encryption Round - A single round of stream encryption. Not used independently.
#
def _aes_encr_round(data: bytes, roundkey: bytes):
    # left 16 is the IV/nonce, all rest beyond byte 16 will be XORd with keystream
    # pass iv, increment per block on iv, to one_ctr_block function per block
    leftbytesin = data[:16]
    rightbytesin = data[16:]
    rightbytesout = b''

    # Split datastream into blocks of 16 bytes
    block = [rightbytesin[i: i+16] for i in range(0, len(rightbytesin), 16)]

    # Now we iterate over each 16 byte block, incrementing iv by 1 for every block
    for i in range(0, len(block)):
        key = _one_ctr_block(roundkey, _increment(leftbytesin, i))
        rightbytesout += _xor_bytes(key, block[i])

    result = leftbytesin + rightbytesout
    return result


# HMAC Generation - Needed for HMAC, takes MAC and Message or content, also used below for HMAC round
#
def _mac_hmac256_generation(message: Union[str, bytes], roundkey: bytes):
    message = message.encode() if isinstance(message, str) else message  # force convert into bytes
    result = hmac.new(roundkey, message, hashlib.sha256).digest()
    return result


# HMAC Round - Part of 4 pass encryption/decryption
#
def _hmac256_round(message: Union[str, bytes], roundkey: bytes):
    message = message.encode() if isinstance(message, str) else message  # force convert into bytes
    leftbytesin = message[:16]
    rightbytesin = message[16:]
    # left 16 is the message and will be XORd with keystream, all rest beyond byte 16 is untouched
    leftbytesout = _xor_bytes(_mac_hmac256_generation(rightbytesin, roundkey), leftbytesin)
    return leftbytesout + rightbytesin


# Main encryption - 4 passes, 1/3 are aes_encr_round, 2/4 are hmac256_round
#
def four_pass_ENCRYPT(key: bytes, plaintext: Union[str, bytes], nonce: bytes):
    k0, k1, k2, k3, k4, k5, k6 = kdf(key, nonce)
    plaintext = plaintext.encode() if isinstance(plaintext, str) else plaintext  # force convert into bytes
    r1 = _aes_encr_round(plaintext, k1)
    r2 = _hmac256_round(r1, k2)
    r3 = _aes_encr_round(r2, k3)
    r4 = _hmac256_round(r3, k4)
    return r4


# Main decryption - 4 passes in reverse, 4/2 are hmac256_round, 3/1 are aes_encr_round,
#
def four_pass_DECRYPT(key: bytes, ciphertext: bytes, nonce: bytes):
    k0, k1, k2, k3, k4, k5, k6 = kdf(key, nonce)
    r1 = _hmac256_round(ciphertext, k4)
    r2 = _aes_encr_round(r1, k3)
    r3 = _hmac256_round(r2, k2)
    r4 = _aes_encr_round(r3, k1)
    return r4


##############################################################################################################################
#  Gonna handle some argparse basics here...
##############################################################################################################################


parser = ArgumentParser(prog='fencrypt.py', description='simple command-line based program to handle some file operations')
FENC_META_STARTS = '.fenc-meta.'

# > OPERATION FLAGS
parser.add_argument('-e', action='store_true', help='encrypt files using protected password.')
parser.add_argument('-d', action='store_true', help='decrypt files using protected password.')
# < -d flag will be set to True later, if no flag was declared
parser.add_argument('-s', action='store_true', help='search decrypted files.')

# > CONTROL FLAGS
parser.add_argument('-j', action='store_true', help='print out key info about files as JSON.')
parser.add_argument('-o', action='store_true', help='print out debugging process.')

# > INPUT FLAG
parser.add_argument('P', nargs='*', help='target files to process, or search terms.')


# ############### encoding and normalizing methods


def encoding_please(file_path: str = None, data: bytes = None):
    # Lets determine if a file is binary or text, it will matter for searching (empty MAC field)

    # first, check that we have inputs
    if file_path is None and data is None:
        raise ValueError('Can not execute with no argument')
    # DECLARING VARIABLES
    BUFFER_SIZE = 1000  # this is the length of bytes to read from the file at once, just to avoid overload the RAM if the file is large
    BOM = b'\xEF\xBB\xBF'
    ANSI, ASCII, UTF8, UTF8_BOM = 'ansi', 'ascii', 'utf-8', 'utf-8-bom'  # constants that one will appear in the result
    result = ASCII  # default result if the file is empty or just english letters
    reminder = 0  # important to use to detect utf-8
    #
    #  RUN THE CHECKING
    file = open(file_path, 'rb') if file_path else None  # open the file if specified
    try:  # to catch any error if happen and close the file
        first_while = True
        while True:  # will keep reading data from the file till no longer data are provided
            if file:  # if there is a file opened
                buffer = file.read(BUFFER_SIZE)  # read as buffer size
                if first_while and buffer.startswith(BOM):
                    result = UTF8_BOM
                    buffer = buffer[3:]
                if len(buffer) == 0:  # this to catch when we have done with the file
                    if data:  # move to process data continuously after file finished
                        buffer = data
                        data = None  # mark as done
                    else:  # break if no data are there or if marked as done
                        break
            elif data:  # if this is a data-mode only, and there are data
                buffer = data  # set data to buffer
                data = None  # mark as done
            else:  # this will be reached only on data-mode and just when data already marked as done (see previous line)
                break
            #
            # LOOP CURRENT BUFFER AND PROCESS IT
            for byte in buffer:
                if byte == 0:  # when there is a null byte
                    return ANSI
                if reminder:  # when we are inside utf-8 bytes discovering
                    if (not byte & 0b10000000) or (byte & 0b01000000):
                        return ANSI  # if this is not a valid utf-8 byte
                    else:  # when this is valid utf-8 byte
                        reminder -= 1  # mark as calculated and continue
                elif byte & 0b11000000 == 0b11000000:  # if this byte has utf-8 starting pattern
                    # detect which utf-8 length it specifies, with make sure it is valid utf-8 starter byte
                    bytes_count = 2 if not byte & 0b00100000 else \
                        3 if byte & (x___ := 0b11100000) == x___ and not byte & 0b00010000 else \
                        4 if byte & (x___ := 0b11110000) == x___ and not byte & 0b00001000 else \
                        5 if byte & (x___ := 0b11111000) == x___ and not byte & 0b00000100 else \
                        6 if byte & (x___ := 0b11111100) == x___ and not byte & 0b00000010 else 0
                    if bytes_count == 0:  # when it is not a valid utf-8 starter
                        return ANSI  # means file can't be utf-8 in any way, and also ASCII because it has the eighth byte, So it is ANSI
                    # when everything went well with this utf-8 starter byte
                    result = UTF8  # make the encoding to be utf-8 for now, and continue checking
                    reminder = bytes_count - 1  # remember how many bytes need to be discovered
                elif byte & 0b10000000:  # when current byte has NOTHING to do with utf-8
                    # test to see if it is ANSI by checking eighth byte
                    return ANSI
                else:  # ASCII is the last to check of, so this must be ASCII 100%
                    pass  # don'T do result = ASCII
            first_while = False
    finally:
        if file and not file.closed:  # close the file if open
            file.close()
    if reminder:  # when the data are completed but still there some missing bytes, return ANSI
        return ANSI
    return result


def get_all_words(data: str, min_=1, max_=100, lower=True, normalize=True):
    # this method does: casefolding and normalization on the run
    pat = re.compile(r'\w{%s,%s}' % (min_, max_))
    result = set()
    for w in pat.findall(data):
        w = w.lower() if lower else w
        w = unicodedata.normalize('NFC', w) if normalize else w
        result.add(w)
    return result


##############################################################################################################
#  Some functions for the purpose of file handling, password collection, etc
##############################################################################################################


def _input_a_password():
    password = getpass.getpass('Enter a password: ')
    return password


def __is_file_encrypted(filename: str):
    return os.path.isfile(FENC_META_STARTS + filename)


def __add_filename_to(_filename: str, to: list, min_size: int = None):
    # Make sure we dont blow up our own file and other valid files
    if os.path.join(os.getcwd(), _filename) == __file__:  # if the current dir is the default one, ignore this python file (Don't touch it)
        print('  Error: can not do operations on this python file program: "{}"'.format(_filename))
        return  # don't add it
    if min_size is not None and os.path.getsize(_filename) < min_size:  # when size is less than required
        print('  Error: file "{}" is less than {} byte!'.format(_filename, min_size))
        return  # don't add it
    to.append(_filename)  # add current file to list


def _get_files(normal_files=False, FENC_META_files=False, all_files=False, min_size: int = None):
    # > when no file type was specified, Error and cancel
    if not (normal_files or FENC_META_files or all_files):
        raise SyntaxError('Error: no file type was declared!')
    # get everything in current directory
    all_filenames = os.listdir()
    #  start processing
    result = []
    for single in all_filenames:  # loop all file and dir names in this directory
        if os.path.isfile(single):  # continue only if this is a file
            if all_files:  # when all files are in demand
                __add_filename_to(single, result, min_size)
            elif FENC_META_files:  # when only meta files in demand
                if single.startswith(FENC_META_STARTS):  # it must be starting with the $FENC_META_STARTS
                    __add_filename_to(single, result, min_size)
            else:  # when only normal files in demand, Not meta files
                if not single.startswith(FENC_META_STARTS):
                    __add_filename_to(single, result, min_size)
    return result


def _process_filenames_for_encryption(filenames: Sequence[str]):
    # Encrypt -  Lets check files exist and has doesnt metadata file, else move on
    result = []
    for filename in filenames:
        if os.path.isfile(filename):
            if __is_file_encrypted(filename):
                print('  File "{}" is ALREADY encrypted!'.format(filename))
            else:
                __add_filename_to(filename, result, 32)
        else:
            print('  Error: file "{}" is not found'.format(filename))
    return result


def _process_filenames_for_decryption(filenames: Sequence[str]):
    # Decrypt - Lets check file exists and HAS  metadata, else move one
    result = []
    for filename in filenames:
        if os.path.isfile(filename):
            if __is_file_encrypted(filename):
                __add_filename_to(filename, result)
            else:
                print('  File "{}" is NOT encrypted!'.format(filename))
        else:
            print('  Error: file "{}" is not found!'.format(filename))
    return result


def encrypt(o_flag: bool, j_flag: bool, filenames: Sequence[str]):

    def encrypt_file(_filename: str):
        # Try to do what we need to here to encrypt the file, and generate metadata
        def create_FENC_META():
            # Lets start to populate the .fenc-meta file of the current file 
            nonlocal FENC_META, _filename  # just declaring that these vars are not on this scope
            buf = json.dumps(FENC_META, indent=4)  # convert dict into string with some formatting
            open(FENC_META_STARTS + _filename, 'w').write(buf)  # write it on a new file (can overwrite olds)

        nonlocal password
        ANSI, ASCII, UTF8, UTF8_BOM = 'ansi', 'ascii', 'utf-8', 'utf-8-bom'  # these are the possible returns by encode_please() method

        # > Generating the master key
        salt = files_properties[_filename]['salt']
        base_key = files_properties[_filename]['base_key']
        nonce0 = files_properties[_filename]['nonce0']
        k0, _k1, _k2, _k3, _k4, _k5, k6 = kdf(base_key, nonce0)  # we'll need k0 for validation here, and possibly k5

        with open(_filename, 'r+b') as file:  # open the current working file, to read and write as binary file
            file_data = file.read()  # get all data from the file
            is_utf_file = True if encoding_please(data=file_data) in [ASCII, UTF8, UTF8_BOM] else False  # check utf-8
            search_terms = []  # default value is no search terms
            if is_utf_file:  # when it is utf-8, get all words and MAC them all
                words = get_all_words(file_data.decode(), 4, 12)  # get all valid words, case folded and NFC normalized
                search_terms = sorted(mac_term(word, k6) for word in words)  # MAC search terms
                #print('search termq:', search_terms)
            #
            # create output file and encrypt data
            validator = k0 # the validator that will be in .fenc-meta file
            mac, encrypted_file_data = encrypt_file_data(file_data, base_key, nonce0)
            # > make the dict of .fenc-meta
            FENC_META = {
                'salt': binascii.hexlify(salt).decode(),
                'validator': binascii.hexlify(validator).decode(),
                'mac': binascii.hexlify(mac).decode(),
                'terms': search_terms
            }
            file.seek(0)  # set the pointer to the start of the file
            file.write(encrypted_file_data)  # overwrite all file data
            create_FENC_META()  # create the .fenc-meta file
            if o_flag:
                print('-file "{}" has been encrypted successfully!'.format(_filename))
            return True

    if o_flag:  # debugging info
        print('Encryption method:')

    files_to_encrypt = _process_filenames_for_encryption(filenames)  # process all given files to see if they exist and not already encrypted
    # > when there are 0 files, error and exit
    valid_files_count = len(files_to_encrypt)
    if valid_files_count == 0:
        print('Error: there are no files to encrypt!')
        if len(filenames) == 0:
            print('  Make sure you passed arguments to the program')
        return False
    if o_flag:  # debugging info
        invalid_files_count = len(filenames) - valid_files_count
        print('  Valid files to encrypt: {}'.format(valid_files_count))
        if invalid_files_count > 0:
            print('  Ignored files: {}'.format(invalid_files_count))

    password = _input_a_password()  # take the password

    files_properties = {}
    for file_name in files_to_encrypt:
        # > Generating the master key
        _salt = secrets.token_bytes(16)  # random salt for each file
        _master_key = hashlib.pbkdf2_hmac('sha256', password.encode(), _salt, 250000, 32)
        _base_key = _master_key[:16]
        _nonce0 = _master_key[16:]
        files_properties[file_name] = {
            'salt': _salt,
            'master_key': _master_key,
            'base_key': _base_key,
            'nonce0': _nonce0
        }

    # > j flag: when -j was declared
    if j_flag:
        print('The requested data as JSON:')
        j_flag_output = {fname: binascii.hexlify(fvalues['master_key']).decode() for fname, fvalues in files_properties.items()}
        print(json.dumps(j_flag_output, indent=4))  # out put the requested data

    fail_counter = 0
    for file_name in files_to_encrypt:  # loop all the files
        try:
            if not encrypt_file(file_name):  # try to encrypt every one within an error handler
                fail_counter += 1
        except Exception as e:
            fail_counter += 1
            print('Unexpected error with file "{}" says : {}'.format(file_name, e))  # this error might raise if the file is already opened by another task
    print('Encryption is completed on {} files, with {} error{}'.format(len(files_to_encrypt), fail_counter, 's' if fail_counter > 1 else ''))


def decrypt(o_flag: bool, j_flag: bool, filenames: Sequence[str]):

    def decrypt_file(_filename: str):
        # Lets decrypt, check validation first and MACs, handle removal of metadata

        def delete_FENC_META():
            #deletes the .fenc-meta file of the current file 
            nonlocal _filename  # just declaring that these vars are not on this scope
            os.remove(FENC_META_STARTS + _filename)

        nonlocal files_metadata, files_properties
        file_metadata = files_metadata[_filename]  # extract metadata of this file
        file_properties = files_properties[_filename]  # extract properties for of file
        # > open file
        with open(_filename, 'r+b') as file:
            file_data = file.read()  # get all file data
            k0, k1, k2, k3, k4, k5, k6 = kdf(file_properties['base_key'], file_properties['nonce'])
            mac = hmac.new(k5, file_data, hashlib.sha256).digest()
            # > decrypt data and get the MAC
            if binascii.hexlify(mac).decode() == file_metadata['mac']:
                file.seek(0)  # point to the top of the file
                plaintext = decrypt_file_data(file_data, file_properties['base_key'], file_properties['nonce'])
                file.write(plaintext)  # overwrite all data
                delete_FENC_META()  # remove metafile
                if o_flag:
                    print('-file "{}" has been decrypted successfully!'.format(_filename))
                return True
            else:
                print('MAC did not validate for: {}'.format(_filename))

    if o_flag:
        print('Decryption method:')

    files_to_decrypt = _process_filenames_for_decryption(filenames)
    # > when there are 0 files, error and exit
    valid_files_count = len(files_to_decrypt)
    if valid_files_count == 0:
        print('Error: there are no files to decrypt!')
        if len(filenames) == 0:
            print('  Make sure you passed arguments to the program')
        return
    elif o_flag:  # debugging info
        invalid_files_count = len(filenames) - valid_files_count
        print('  Valid files to decrypt: {}'.format(valid_files_count))
        if invalid_files_count > 0:
            print('  Ignored files: {}'.format(invalid_files_count))

    password = _input_a_password()

    # > Generate the password validator and key schedule for each file
    files_metadata = {}  # filenames as keys, .fenc-meta info as values (after converting them into python dictionary)
    files_properties = {}  # filenames as keys, validators and key schedule as values
    # > loop all files needs to be decrypted
    for file_name in files_to_decrypt:
        try:
            fencmeta_file_name = FENC_META_STARTS + file_name  # generate the .fenc-meta file name
            with open(fencmeta_file_name, 'r') as FENC_META_file:
                files_metadata[file_name] = json.loads(FENC_META_file.read())  # read .fenc-meta file data
            #
            salt = bytes.fromhex(files_metadata[file_name]['salt'])  # read the salt from .fenc-meta file
            # > Generate the master key and other keys and validator from given password and recovered salt
            master_key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 250000, 32)
            base_key = master_key[:16]
            nonce0 = master_key[16:]
            k0, _k1, _k2, _k3, _k4, _k5, k6 = kdf(base_key, nonce0)  # we need to use is k0, the validator and k6, the mac
            validator = k0
            files_properties[file_name] = {  # save these keys to be used later to compare and decrypt the files
                'salt': salt,
                'master_key': master_key,
                'base_key': base_key,
                'nonce': nonce0,
                'validator': binascii.hexlify(validator).decode(),  # this one is used just for comparing
            }
        except Exception as e:
            print('Cannot perform metadata processing with file "{}"'.format(file_name))
            print('    Message says: {}'.format(e))

    # > if -j flag is True, Show a dict of keys as filenames, and hex-encoded 32-byte output of PBKDF2 (master key) associated with each file
    if j_flag:
        # create a dictionary of filenames as keys, and as values the hex-encoded 32-byte output of PBKDF2 associated with each file
        # from the current given password, master key needs to be hexlified
        j_flag_output = {fname: binascii.hexlify(fvalues['master_key']).decode() for fname, fvalues in files_properties.items()}
        print('The requested data as JSON:')
        print(json.dumps(j_flag_output, indent=4))

    # > Compare password validator and error with no decryption if not match
    # compare validator that just created by current password with the one in metadata, of each file
    # and keep just the matched files in "validated_files", and throw error files to "unvalidated_files"
    validated_files = []
    unvalidated_files = []
    for file_name in files_to_decrypt:
        if files_properties[file_name]['validator'] == files_metadata[file_name]['validator']:
            validated_files.append(file_name)  # matches
        else:
            if len(unvalidated_files) == 0:  # when nothing was inserted yet, print the first message
                print()
                print('PASSWORD DID NOT MATCH WITH THESE FILES:')
            unvalidated_files.append(file_name)  # did not match
            print('   ', file_name)  # show error file

    if len(validated_files) == 0:
        print('Error: there are no files to decrypt!')
        return
    fail_counter = 0
    for filename in validated_files:
        try:
            decrypt_file(filename)
        except Exception as e:
            print('Unexpected error with file "{}" says : {}'.format(filename, e))
    print('Decryption is completed on {} files, with {} error{}'.format(len(validated_files), fail_counter, 's' if fail_counter > 1 else ''))


def search(o_flag: bool, j_flag: bool, terms: Sequence[str]):
    if o_flag:
        print('Searching method:')
        print('  search terms: "' + '", "'.join(terms) + '"')

    files_to_search = _get_files(FENC_META_files=True)
    valid_files_count = len(files_to_search)
    if valid_files_count == 0:
        print('Error: there are no files to perform the search operation!')
    elif o_flag:
        print('  Files found to search: {}'.format(valid_files_count))

    password = _input_a_password()

    # If password validator for a file doesn't match, warn to stderr, one line per file that fails
    # For each file where the password validator did match, perform the search operation
    # If -j flag is given, output key info only for files the password validator matches, and before providing output
    # For each file matches, output one line to stdout for each match indicating filename and nothing else
    # If no files match the search term you may optionally output error to stderr


def director(args: Namespace):
    # direct the process to the right method
    if args.e:
        encrypt(args.o, args.j, args.P)
    elif args.d:
        decrypt(args.o, args.j, args.P)
    elif args.s:
        search(args.o, args.j, args.P)
    else:
        # > This error shouldn't appear, if it did, please check the functionality of setting a default flag when None was declared
        raise RuntimeError('Error: no operator has been used!')


if __name__ == '__main__':

    # get arguments ready to parse
    sys_args = sys.argv[1:]

    # > parse the script arguments with ArgumentParser
    parsed_args = parser.parse_args(sys_args)

    # set default -d if no operator arguments
    if not (parsed_args.e or parsed_args.d or parsed_args.s):
        parsed_args.d = True

    # check if only one of (e, d, s) was declared, error otherwise
    declared_eds_flags = sum((parsed_args.s, parsed_args.d, parsed_args.e))
    #error_msg = None
    if declared_eds_flags > 1:
        error_msg = 'Error: only one operator flag can be used (-e or -d or -s)!'

    # start our function calls as per request from args
    director(parsed_args)
