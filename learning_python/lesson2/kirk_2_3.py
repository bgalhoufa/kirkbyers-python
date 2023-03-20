#/usr/bin/env python3

from pprint import pprint

with open('show_arp.txt') as f:
    output = f.readlines()

my_list1 = (output[1:])

my_list2 = (my_list1[:3])

#pprint(my_list2)

my_list2 = "\n".join(my_list2)

with open("arp_entries.txt", "wt") as f:
    f.write(my_list2)
