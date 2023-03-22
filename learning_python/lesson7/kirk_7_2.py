#!/usr/bin/env python3

import jinja2

template_file = "ospf.j2"
with open(template_file) as f:
    jinja_template = f.read()


act_intf = ['Vlan1', 'Vlan2']
area0_netw = ['10.10.10.0/24', '10.10.20.0/24', '10.10.30.0/24']

template_vars = {
        'ospf_process_id':'10',
        'ospf_priority':'100',
        'ospf_active_interfaces': act_intf,
        'ospf_area0_networks': area0_netw
        }
template = jinja2.Template(jinja_template)
print(template.render(template_vars))

