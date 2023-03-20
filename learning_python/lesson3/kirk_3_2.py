#!/usr/bin/env python3

from pprint import pprint

with open('show_arp.txt') as f:
    output = f.readlines()

my_data = []

for i in output:
    my_list = i.split()
    #print(my_list)
    if my_list[0] == 'Internet':
        ip_addr = my_list[1]
        mac_addr = my_list[3]
        my_data.append((ip_addr, mac_addr))

for ip in my_data:
    if '10.220.88.1' in ip:
        print(f'Default gateway IP/Mac is {ip}')
    elif '10.220.88.30' in ip:
        print(f'Arista3 IP/Mac is {ip}')
        break

#pprint(my_data)
