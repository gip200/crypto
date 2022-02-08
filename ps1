#!/usr/bin/env python3

# from nacl.secret import SecretBox
# from nacl.exceptions import CryptoError
import sys
import json
import binascii
import random

# Func to sort ip's
def sort_ips(ip_list):
    # List to split IPs in list of list
    sorted_ips = []
    for ip in ip_list:
        ip_split = [int(element) for element in ip.split(".")]
        sorted_ips.append(ip_split)
    sorted_ips.sort()

    # Join the list of list to IPs and append to final result
    result = []
    for ip_split in sorted_ips:
        ip_split = [str(element) for element in ip_split]
        ip = ".".join(ip_split)
        result.append(ip)

    # Return result
    return result


inputs = json.load(sys.stdin)
outputs = {}

# problem 1
input_string = inputs["problem 1"]
for i in range(len(input_string)):
    input_string[i] = input_string[i].upper()
outputs["problem 1"] = input_string

# problem 2
input_hex2 = inputs["problem 2"]
output_string2 = []
for i in range(len(input_hex2)):
    input_hex2[i] = (input_hex2[i])
    output_bytes = bytes.fromhex(input_hex2[i])
    output_ascii = output_bytes.decode()
    output_string2.append(output_ascii)
outputs["problem 2"] = output_string2

# problem 3
input_hex3 = inputs["problem 3"]
output_string3 = []
split_hex3 = []
concat_hex = ""
preoutput_string3 = ""
newstr = ""

for index1 in range(len(input_hex3)):
    input_hex3[index1] = (input_hex3[index1])
    workinghex = input_hex3[index1]
    #print(workinghex)

    split_hex3 = [workinghex[index2: index2 + 2] for index2 in range(0, len(workinghex), 2)]
    #print(split_hex3)

for index3 in range(len(split_hex3)):
        split_hex3[index3] = hex(int((split_hex3[index3]),16) + 32 + index3).lstrip("0x")
        concat_hex += split_hex3[index3]
        newstr = concat_hex
        #print(concat_hex)
        #print(newstr)

output_string3.append(newstr)

#print(output_string3)
outputs["problem 3"] = output_string3

# problem 4
input_strings_4 = inputs["problem 4"]
output_string_4 = []

for index4 in range(len(input_strings_4)):
    input_strings_4[index4] = (input_strings_4[index4])
    input_strings_4[index4] = random.randrange(0, input_strings_4[index4]-1)
    output_string_4.append(input_strings_4[index4])

outputs["problem 4"] = output_string_4


# output
#json.dump(outputs, sys.stdout)
print(json.dumps(outputs, indent="  "))
print()
