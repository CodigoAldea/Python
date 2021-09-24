'''Write a Python program to print a specified list after 
removing the 0th, 4th and 5th elements.'''

a = [1,2,3,4,5,6,7,8]
b = [0,4,5]
c=[]
for i in range(len(a)):
    if i not in b:
        c.append(a[i])
        print(i)
print(c)
