#!/usr/bin/env python3

from pprint import pprint

with open('show_vlan.txt') as f:
    output = f.readlines()

output1 = output[2:]

output1.pop(1)

#pprint(output1)

vlan_list = []

for i in output1:
    output2 = i.split()
    vlan_id = output2[0] 
    vlan_name = output2[1]
    vlan_list.append((vlan_id, vlan_name))

pprint(vlan_list)


