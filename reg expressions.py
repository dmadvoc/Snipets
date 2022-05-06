# Regular Expressions
# This is python's way of doing wildcards. It's its own language
# It is a shortcut language that can be done with other sring commands
""" ###########################
^ Match the start of a line
* Many times
. Match any character
\S Non whitespace characters
###############################"""

import re

# Find and print line that have From:
fhand=open('Readfile.txt')
#print(fhand.read())
for line in fhand:
    line=line.rstrip()
    if line.find('From:')>=0:
        print(line)

# Now use Regular Expressions to Find and print line that have From:
fhand=open('Readfile.txt')
for line in fhand:
    line=line.rstrip()
    if re.search('From:', line):
        print(line)