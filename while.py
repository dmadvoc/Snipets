# While loops require an iteration step, e.g. n+1

# simple while loop
n = 0
while n <= 1_000:
    print(n)
    n = n + 200

# Simple loop with an output array
# NOTE: it is IMPORTANT to put the .append before the iteration
 # Otherwise you'll get an endless loop
out=[]
n=0
while n <= 1_000:
    #print(n)
    out.append(n)
    n = n + 200
print(out)