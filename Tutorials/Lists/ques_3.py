'''Write a Python program to print a specified list after 
removing the 0th, 4th and 5th elements.'''

a = [1,2,3,4,5,6,7,8]
b = [0,4,5]
for i in range(len(a)):
    if i in b:
        a.remove(a[i])
print(a)