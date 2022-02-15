#!/usr/bin/env python3

import sys
import json
import binascii
import secrets

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
workinghex = {}
split_hex3 = []
concat_hex = ""
newstr = ""

for index1 in range(len(input_hex3)):
    input_hex3[index1] = (input_hex3[index1])
    workinghex = input_hex3[index1]
    #print(workinghex)

    split_hex3 = [workinghex[index2: index2 + 2] for index2 in range(0, len(workinghex), 2)]
    #print(split_hex3)
    outpass = split_hex3

    for index3 in range(len(outpass)):
      outpass[index3] = (hex((int((outpass[index3]),16) + 32 + index3) % 256).lstrip("0x"))
      #print (split_hex3[index3])
      concat_hex += outpass[index3]
      #print(concat_hex)
      
    output_string3.append(concat_hex)
    concat_hex = ""

#print(output_string3)
outputs["problem 3"] = output_string3

# problem 4
input_strings_4 = inputs["problem 4"]
output_string_4 = []

for index4 in range(len(input_strings_4)):
    input_strings_4[index4] = (input_strings_4[index4])
    input_strings_4[index4] = secrets.randbelow(input_strings_4[index4]-1)
    output_string_4.append(input_strings_4[index4])

outputs["problem 4"] = output_string_4

#output
#json.dump(outputs, sys.stdout)
print(json.dumps(outputs, indent="  "))
print()
