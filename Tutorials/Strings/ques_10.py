'''Write a Python program to remove all consecutive duplicates of a given string.'''

n = input('Enter a String : ')
m = ""
for i in n:
    if i not in m:
        m += i
print ('New String : ', m)