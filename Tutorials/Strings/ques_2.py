'''Write a Python program to get a string from a given string where all 
occurrences of its first char have been changed to '$', except the first char itself.'''

n = input('Enter the string :')
x = ''
for i in n:
    if i in x : 
        i = '$'
        x+=i
    else:
        x+=i
print (x)