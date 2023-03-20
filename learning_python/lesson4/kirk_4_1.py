#!/usr/bin/env python3

my_dict = {'ip_add':'10.10.10.10', 'vendor':'cisco', 'username':'admin', 'password':'Cisco1234'}

my_bgp_fields = {'bgp_as':'65535', 'peer_as':'429496', 'peer_ip':'10.5.5.5'}

#print(my_dict['ip_add'])


for key,value in my_dict.items():
    if key == 'vendor' and value == 'cisco':
        is_cisco = True
    elif key == 'vendor' and value == 'juniper':
        is_juniper = True

if is_cisco == True:
    dict_platform = {'platform':'ios'}
    my_dict.update(dict_platform)
elif is_juniper == True:
    dict_platform = {'platform':'junos'}
    my_dict.update(dict_platform)

my_dict.update(my_bgp_fields)

for key in my_dict:
    print(key)

#print(my_dict)
