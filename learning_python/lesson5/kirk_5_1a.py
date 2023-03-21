#!/usr/bin/env python3

def ssh_conn(ip_addr, username, password):
    print(f'The IP is {ip_addr}; the username is {username}; the password is {password}')


#ssh_conn('10.10.10.10', 'admin', 'Cisco1234')
#ssh_conn(ip_addr='10.10.10.10', username='admin', password='Cisco1234')
ssh_conn('10.10.10.10', 'admin', password='Cisco1234')
