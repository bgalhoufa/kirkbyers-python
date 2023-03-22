#/usr/bin/env python3

import jinja2

int_vars = {
        'vlan':'400',
            'name':'red400'
            }

int_template = '''
vlan {{ vlan }}
    name {{ name }}
'''

my_temp = jinja2.Template(int_template)
print(my_temp.render(int_vars))
