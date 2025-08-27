"""Fix custom-reporter.js path issues in Dockerfiles.

The main issues are:
1. Some Dockerfiles use WORKDIR /app instead of /testbed
2. Some have chmod commands pointing to wrong paths
"""
import sys

dockerfile_content = sys.argv[1]

if 'custom-reporter.js' not in dockerfile_content:
    print(dockerfile_content)
    sys.exit(0)

lines = dockerfile_content.split('\n')
fixed_lines = []

for line in lines:
    # Fix WORKDIR to use /testbed instead of /app
    if line.strip() == 'WORKDIR /app':
        fixed_lines.append('WORKDIR /testbed')
    # Fix chmod commands that point to /app instead of /testbed
    elif 'chmod +x /app/custom-reporter.js' in line:
        fixed_lines.append(line.replace('/app/custom-reporter.js', '/testbed/custom-reporter.js'))
    else:
        fixed_lines.append(line)

print('\n'.join(fixed_lines))
