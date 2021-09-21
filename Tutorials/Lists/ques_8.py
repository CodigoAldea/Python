'''Write a Python program to insert an element before each 
element of a list.'''

a = [1,2,3,4]
# variable is c
a= [v for i in a for v in('c',i)]
print(a)