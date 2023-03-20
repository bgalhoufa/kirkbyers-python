#/usr/bin/env python3

from pprint import pprint

with open('show_ip_int_brief.txt') as f:
    output = f.readlines()

output2 = output[5]

output3 = output2.split()

output4 = (output3[0], output3[1])

pprint(output4)
