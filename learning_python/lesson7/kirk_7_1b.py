#/usr/bin/env python3

import jinja2

encr_vars = {
        'encr':'aes',
        'group':'5',
        'isakmp_enable': False
            }


encr_template = '''
{%- if isakmp_enable %}
crypto isakmp policy 10
 encr {{ encr }}
 authentication pre-share
 group {{ group }}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{% endif %}
'''

my_temp = jinja2.Template(encr_template)
print(my_temp.render(encr_vars))
