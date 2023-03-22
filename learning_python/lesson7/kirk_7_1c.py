#/usr/bin/env python3

import jinja2

my_vlans = {
 '501':'blue501',
 '502':'blue502',
 '503':'blue503',
 '504':'blue504',
 '505':'blue505',
 '506':'blue506',
 '507':'blue507',
 '508':'blue508',
 }

vlan_vars = {'vlans': my_vlans}



vlan_template = '''
{%- for vlan, name in vlans.items() %}
vlan {{ vlan }}
   name {{ name }}
{% endfor %}
'''

my_temp = jinja2.Template(vlan_template)
print(my_temp.render(vlan_vars))
