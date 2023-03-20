#!/usr/bin/env python3

from pprint import pprint

my_ip_addr = '10.10.100.'

my_range = range(1, 255)

my_ip = []

for number in my_range:
    my_ip.append((my_ip_addr, str(number)))
    full_list = [''.join(ips) for ips in my_ip]

new_list = full_list[2:6]

for ip in new_list:
    print(f'O IP que vamos pingar agora é: {ip}')

#pprint(new_list)
