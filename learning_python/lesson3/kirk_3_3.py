#!/usr/bin/env python3

from pprint import pprint

with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.read()

system_name, port_id = (None, None)

#pprint(show_lldp.splitlines())

for line in show_lldp.splitlines():
    if "System Name: " in line:
        _, system_name = line.split("System Name: ")
    elif "Port id: " in line:
        _, port_id = line.split("Port id: ")

    if port_id and system_name:
        break

print()
print("System Name: {}".format(system_name))
print("Port ID: {}".format(port_id))
print()

