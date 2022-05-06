#readfile.txt in he file to type in
# Try typing a bad file name

fhand=input('type file name: ')
try:
    fhand=open(fhand)
except:
    print('Cannot open bad file name: ', fhand) #this isn't printing?
    quit()

  
fhand=open('readfile.txt') # file handle opens text file
inp=fhand.read()           # Reads the file as input
print(inp)                
print(len(inp))            # Length of file is 106 characters
print(inp[:20])            # Prints the first 19 characters 