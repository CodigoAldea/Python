'''Write a Python program to check if a specified element is presents in a tuple of tuples.'''

t = ((1,2,3), (4,5,6), (7,8,9))
n = int(input('enter a number :'))
r = any(n in i for i in t)
if r == True:
    print(n, ': is present ')
else : 
    print(n, ": is not present")