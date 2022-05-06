# Tuples
# Tuples are a kind of list and use parenthesis (), e.g. (1,2,3)
# Tuples are immutable unlike lists, ie. can't sort or replace or append tuples
# Tuples are more efficient for storage and operations
# Tupes are comparable, retuning a boolean, only compares leftmost values
# Can sort a list of tuples

t=tuple()
dir(t)     # you can only count and index tuples

# Assignment
x=(1, 'Fred')
print(x)

(a,b)=(1,'Fred')
print(a,b)

# looping through tuples
x=dict()
x['ears']=2
x['nose']=1
for (k,v) in x.items():
    print(k,v)

tups=x.items()
print(tups)

# Comparing tuples, works form left to right
(1, 10, 1000) == (1, 10, 1000)  # True b/c 1 =1, doest look at next pair
(1, 10, 5000) <= (1, 11, 2000)  # True b/c 10 < 11, doesnt look at next pair
(1, 10, 1000) >= (1, 10, 2000)  # True b/c 2000 > 1000
('Pear', 'Apple') > ('Apple', 'Pear')
('Joe', 'Sal') < ('Joe', 'Sam') # True b/c Sal < Sam

# Sort a list of tuples, first sorts by key then by value
d={'a':5, 'c':10, 'b':20}
d.items()
sorted(d.items())
# can loop through it, note the k, v can be w/o or w/ ()
for k, v in sorted(d.items()):
    print(k, v)
    
# Make a list of tuples and flipping key and value

tmp=list()    
for k, v in d.items():
    tmp.append((v, k))  #note the double parenthesis(())
print(tmp)
tmp=sorted(tmp, reverse=True)
print(tmp)    

# Read file and histogram the words
fhand=open('Readfile.txt')
counts=dict()          # Creat dictionary of words w/ counts
for line in fhand:
    words=line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
print(counts)
 
###### 2nd half ##############       
lst=list()             # Create a list of tuples 
for key, val in counts.items():
    newtup=(val, key)
    lst.append(newtup)
lst=sorted(lst, reverse=True)
print(lst)

for val, key in lst[:10]:  # Print the 1st 10 with the most count
    print(key, val)
###### End 2nd half ###########   

# Short hand method for 2nd half
c={'a':10, 'b':1, 'c':22}
print (sorted([(v,k) for k,v in c.items()]))


    
