#!/usr/bin/env python3

my_list1 = ['10.10.0.1', '10.50.40.1', '10.110.0.1', '10.150.40.2', '10.10.0.1', '10.50.40.1', '10.210.0.1', '10.90.40.1', '10.30.0.1', '10.90.40.1']

my_list2 = ['10.20.0.2', '10.40.40.2', '10.110.0.2', '10.150.40.2', '10.10.0.1', '10.50.40.1', '10.210.0.2', '10.90.40.2']

my_list3 = ['10.30.0.3', '10.30.40.3', '10.120.0.3', '10.120.40.3', '10.10.0.1', '10.50.40.1', '10.210.0.3', '10.90.40.3']

my_set1 = set(my_list1)
my_set2 = set(my_list2)
my_set3 = set(my_list3)

print(f'The IPs that are duplicated between Houston and Atlanta are {my_set1 & my_set2}')
print(f'The IPs that are duplicated between Houston, Atlanta and Chicago are {my_set1 & my_set2 & my_set3}')
print(f'The IPs that are unique in Chicago are {my_set3 - my_set2 - my_set1}')
#print(my_set1.intersection(my_set2))
#print(my_set1)
