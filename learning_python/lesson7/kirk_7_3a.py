#!/usr/bin/env python3

import yaml
from pprint import pprint

my_file = 'interfaces.yml'

with open(my_file) as f:
    output = yaml.safe_load(f)

print(output)
