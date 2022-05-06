# Exploring Srings

# For a string
name='David Advocate'
print(len(name))
print(name[2], name[-1])

# Use a loop to tet the index location for each letter in name
 # Note that spaces are an index location
 
# While Loop
index=0
while index < len(name):
    letter = name[index]
    print(letter, index)
    index=index+1

# For Loop 
for letter in name:  # Prints each letter loop-wise
    print (letter)
    
# How many "a" letters in name
count=0
for letter in name:
    if letter == 'a':
        count=count+1
print(count)

# Slicing the strings
 """ The second number is upto but not including - so go one byond
     If the second is beyond the length of the string, it stops
     at the end """
print(name[0:5])    # prints the 1st 5 letters 
print(name[5])      # This should be a space
print(name[6:100])  # Starts on 7th letter to the end
print(name[:2])     # Prints the first 2 letters
print(name[2:])     # Starts on 3rd letter to end
print(name[:])      # Prints entire string

# "in" operator works on stings and returns a boolean
print('a' in name)
print('ate' in name)
if 'vid' in name:
    print("Your're cool")
    
# Compare strings based on sort order. String sorting is case sensitive
a='Banana'
b='Apple'

if a=='Banana':
    print('Yep it is a banana')

if a < b:
    print('a is less than b')
else:
    print('b is less than a')
    
# .upper and .lower built-in print functions
print(a.upper())
print(a.lower())

# Find the data type
type(name)

# List all the things you can do to a specified string
dir(name)
print(name.find('ate'))              #Returns the index of ate
print(name.replace('David', 'Dave')) #original sting unaffected
print(name.replace('a','XXX'))

# Strip "white space" in strings
greet='  Hello World   '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# Startwith returns a boolean
print(name.startswith('D'))
print(name.startswith('A'))

# Find and strip out the host form an email message
data='From dmadvoc@gmail.com Feb 2 2021'
start=data.find('@')      # finds the position of the @
print(start)
stop=data.find(' ',start) # Finds the first space after the @
print(stop)
host=data[start+1:stop]   # Strips out gmail.com from email
print(host)

# for a list of strings
string=['a', 'b', 'c','My name is David Advocate']
print(len(string))            # The array list has a lenght of 4
print(string[2], string[-1])



