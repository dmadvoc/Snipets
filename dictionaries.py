# Dictionarys - associative arrays
# arrays have indexs, dictionary have keys-value pairs
# both the array and dict use [] for position assignment

bag=dict()
bag['meat']=12
bag['vegg']=10
bag['bread']=1
print(bag)
print(bag['meat'])
bag['bread']=bag['bread']+2**2   # calculat
bag['bread']=100                 # overwrite
print(bag['bread'])
bag['bread']=101
print(bag['bread'])

# Dictionary literals use {} to contain key:value pairs
# Assigning a dictionary can use var{} or dict()
  # The curly braces are a short cut without have to initiate w dict()

# Create a associative array, short cut method
aaa={'Dave':1, 'Mary':2 , 'Tiana':3, 'Mariah': 4}
print(aaa)

#Test for an item Dict
'Bob' in aaa

#Add an item to Dict
aaa['Bob']=5
print(aaa)

# Use the in operator and make a count of names
counts=dict()
names=['Bob', 'Bob', 'Bob', 'Tom', 'Ray']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

# .get function looks in the dict and gets the value, else returns a default value
x= counts.get('Ray', 0)
print(x)

# Same loopas before but uses the .get
counts=dict()
names=['Bob', 'Bob', 'Bob', 'Tom', 'Ray']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)

# Loop through text to get a histogram of words
text='the dog ran after the cat and the cat ran after the bird and the bird ate the worm'
words=text.split()
print(words)
counts=dict()
for word in words:
    counts[word]=counts.get(word,0)+1
print(counts)

# Get a list of keys with thir counts
for key in counts:
    print(key, counts[key])
# Other ways to examine a dictionary    
print(list(counts))     # outputs a list of keys only
print(counts.keys())    # outputs a list of keys only
print(counts.values())  # outputs a list of values only
print(counts.items())   # outputs a list of tuples

# interate through a list of tuples - feature unique to Python
for a,b in counts.items():
    print(a,b)
    
# Find the biggest word and value in counts, i.e. the max
bigword=None
bigcount=None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count
print(bigword, bigcount)