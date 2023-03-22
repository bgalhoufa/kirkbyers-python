#!/usr/bin/env python3

import yaml
import jinja2

yaml_file = "interfaces2.yml"
with open(yaml_file) as f:
    template_vars = yaml.safe_load(f)


template_file = "interface_config_ex4.j2"
with open(template_file) as f:
    jinja_template = f.read()


template = jinja2.Template(jinja_template)
print(template.render(template_vars))

