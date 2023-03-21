#!/usr/bin/env python3

import random
last_octet = str(random.randint(1, 254))


def my_func(base_network='10.10.10.'):
    print(f'{base_network}{last_octet}')

my_func('172.16.30.')
