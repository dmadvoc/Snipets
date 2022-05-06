# Reading and working with text files
# Text files are a sequence and each line is a string
# Inbedded in the end of each line is a Newline (\n)

# Open, read and print the textfile
fhand=open('readfile.txt') # file handle opens text file
inp=fhand.read()           # Reads the file as input
print(inp)                
print(len(inp))            # Length of file is 106 characters
print(inp[:20])            # Prints the first 20 characters 

# Iterate through each line in the sequence: each line is a string
fhand=open('readfile.txt') # Have to open this file each time
for anyvalue in fhand:
    print(anyvalue)        # Prints every line in fhand with Newlines (\n)
                           # Note the print function embeds another Newline

# Count the number of lines in the file
fhand=open('readfile.txt') # Have to open this file each time
count=0
for line in fhand:
    count=count+1
print('Number of line in fhand file: ', count)

# Retrieve each line that has "From" in it
fhand=open('readfile.txt')      # Have to open this file each time
for line in fhand:
    if line.startswith('From'):
        print(line)             # Prints each line w/ From + \n

# Use .rstrip to remove white space (\n)
fhand=open('readfile.txt')      # Have to open this file each time
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)  

# This is just another way to print the lines that start with From
fhand=open('readfile.txt')      # Have to open this file each time
for line in fhand:
    line = line.rstrip()
    if not 'From' in line:
        continue
    print(line)  


           



