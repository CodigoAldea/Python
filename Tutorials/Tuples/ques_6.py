'''Write a Python program to remove an item from a tuple.'''

'''option 1
t = ( 1,3,4,5,6,7,8)
t = t[:2] + t[4:]
print(t)'''

'''option 2 
t = ( 1,3,4,5,6,7,8)
l = list(t)
l.remove(l[2])
l.remove(l[3])
t = tuple(l)
print(t)'''