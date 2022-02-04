#!/usr/bin/env python3

#from nacl.secret import SecretBox
#from nacl.exceptions import CryptoError
import sys
import json
import binascii

inputs = json.load(sys.stdin)
outputs = {}

#problem 1
input_string = inputs["problem 1"]
for i in range(len(input_string)):
    input_string[i] = input_string[i].upper()
outputs["problem 1"] = input_string

#problem 2
input_hex = inputs["problem 2"]
output_string2 = []
for i in range(len(input_hex)):
    input_hex[i] = (input_hex[i])
    output_bytes = bytes.fromhex(input_hex[i])
    output_ascii = output_bytes.decode()
    output_string2.append(output_ascii)
outputs["problem 2"] = output_string2

#problem 3
#input_string = inputs["problem 3"]
#output_bytes = input_string.encode()
#output_hex = output_bytes.hex()
#outputs["problem 3"] = output_hex

# Problem 4
#ciphertext_hex = inputs["problem 4"]
#ciphertext_bytes = bytes.fromhex(ciphertext_hex)
#key = b"A" * 32
#nonce = b"B" * 24
#plaintext_bytes = SecretBox(key).decrypt(ciphertext_bytes, nonce)
#plaintext_string = plaintext_bytes.decode()
#outputs["problem 4"] = plaintext_string

# Problem 5
#ciphertext_list = inputs["problem5"]
#key = b"C" * 32
#nonce = b"D" * 24
#for ciphertext_hex in ciphertext_list:
#    ciphertext_bytes = bytes.fromhex(ciphertext_hex)
#    try:
#        plaintext_bytes = SecretBox(key).decrypt(ciphertext_bytes, nonce)
#    except CryptoError:
#        # Bad ciphertext
#        continue
#    plaintext_string = plaintext_bytes.decode()
#    outputs["problem5"] = plaintext_string
#    break

#output
#json.dump(outputs, sys.stdout)
print(json.dumps(outputs, indent="  "))
print()
