'''Write a Python program to count the number of characters (character frequency) in a string.'''

a = input(' Enter a string : ')
f = {}
for i in a :
    if i in f:
        f[i]+=1
    else :
        f[i] = 1
print (' Frequncy of all the characters : ',f)