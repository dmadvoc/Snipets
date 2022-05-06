# Lists are a collection of items signified by []
# Can be strings, intergers or floats
# Strings are not mutable (changable), they have to be changed in a new variable name

# floats and integers are mutable, e.g
ints=[1,2,3,4] #original list
ints[3]=17     #change value in index 3 to 17
print(ints)

things=[1,2,'red',3.1]
print(len(things))     #returns the number of items in things

print(range(4))                    # print "range(0,4)' = [0,1,2,3]
friends=['Peter','Paul','Mary']
print(len(friends))                # returns a value of 3
print(range(len(friends)))         # print "range(0,3)

x=range(4)
for i in x:
    print(i)

for friend in friends:
    print('Hello my friend: ', friend)

# List concatenation
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

# List slicing (just like string)
t=[1,2,3,4,5,6,7,8,9,10]
t[1:6] # two through six
t[:3]  # starts at 0 to three
t[3:]  # starts at four
t[:]   # the whole list

# Things you can do with lists
x=list()  # "constructor form to make empty list, can also use []
type(x)   # Tells you the Dtype
dir(x)    # List all the thing you can do, e.g. sort, remove, insert ....
x.append('book')
x.append(20)
print(x)

# In operators - return booleans
y=[1,2,3,4,5,6,7,8,9,10]
2 in y        # Returns a boolean
0 in y
2 not in y

print(len(y))
print(min(y))
print(max(y))
print(sum(y))
print(sum(y)/len(y)) # This give an average


# Sorting
names = ['Joe', 'Sal', 'Ben']
names.sort()
print(names)
names[1]     # Unlike strings, lists a mutable, -> Joe is the answer

# Convert a string to a list
words='My name is Dave'
abc=words.split()
print(abc)

# Split also works on delimters
words='My,name,is, Dave'
words.replace(" ", "") # This removes all white space
abc=words.split(',')   # spit will carry spaces to the list
print(abc)

