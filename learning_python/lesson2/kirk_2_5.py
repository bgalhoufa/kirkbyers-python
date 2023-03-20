#/usr/bin/env python3

from pprint import pprint

with open("show_ip_bgp_summ.txt") as f:
    bgp_summ = f.readlines()

#bgp_summ = bgp_summ.splitlines()

first_line = bgp_summ[0]
as_number = first_line.split()[-1]
print("Local AS Number: {}".format(as_number))

last_line = bgp_summ[-1]
peer_ip = last_line.split()[0]
print("BGP Peer IP Address: {}".format(peer_ip))

