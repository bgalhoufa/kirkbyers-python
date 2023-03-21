#!/usr/bin/env python3

def ssh_conn(ip_addr, username, password, device_type='cisco_ios'):
    print(f'The IP is {ip_addr}; the username is {username}; the password is {password}; the device type is {device_type}')


my_dict = { 'ip_addr': '10.130.130.1',
        'username': 'warpcom',
        'password': 'Cisco123',
        'device_type': 'juniper_os',
        }


ssh_conn(**my_dict)
#ssh_conn('10.10.10.10', 'admin', 'Cisco1234')
#ssh_conn(ip_addr='10.10.10.10', username='admin', password='Cisco1234')
#ssh_conn('10.10.10.10', 'admin', password='Cisco1234')
