import json
import jinja2
import os

# Declare variables for files and outputs
template_file = "accesssw.j2"
json_file = "params.json"
output_directory = "output"


# Load JSON file
config_params = json.load(open(json_file))

# Setup environment for Jinja2
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath='.'), trim_blocks=True, lstrip_blocks=True)

template = env.get_template(template_file)

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

print("Creating Templates....")
for params in config_params:
    result = template.render(params)

    f = open(os.path.join(output_directory,params['hostname'] + ".config"), "w")
    f.write(result)
    f.close()
    print("Template Created")

