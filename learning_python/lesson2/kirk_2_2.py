#/usr/bin/env python3

my_list = ['10.1.1.1', '10.2.2.2', '10.3.3.3', '10.4.4.4', '10.5.5.5']

my_list.append('10.6.6.6')

print(f'The appended list is {my_list}')

my_list2 = ['10.7.7.7', '10.8.8.8']

my_list.extend(my_list2)

print(f'The extended list is {my_list}')

my_list3 = ['10.9.9.9', '10.10.10.10']

for i in my_list3:
    my_list.append(i)

print(f'The list concatenation is {my_list}')

my_list.pop(0)
my_list.pop(-1)

print(f'The list popped is {my_list}')

my_list.insert(0, '2.2.2.2')

print(f'The list inserted is {my_list}')
