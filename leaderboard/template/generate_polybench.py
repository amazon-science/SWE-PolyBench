import json
from jinja2 import Environment, FileSystemLoader

"""
usage: python generate_polybench.py

Make sure Jinja2 is installed
"""

# Set up Jinja2 environment
env = Environment(
    loader=FileSystemLoader('.'),
    trim_blocks=True,
    lstrip_blocks=True
)

# Load the template
template_polybench = env.get_template('template_polybench.html')

# Load JSON data
with open('polybench_data.json', 'r') as f:
    data = json.load(f)

# Render the template with the data
output_html_polybench = template_polybench.render(data)

# Write the output to a new HTML file
with open('../polybench.html', 'w') as f:
    f.write(output_html_polybench)

print("PolyBench page generated successfully!")
