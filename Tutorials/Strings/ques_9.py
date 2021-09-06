'''Write a Python program to move all spaces to the front of a given string in single traversal.'''

n = input('Enter a string : ')
m = [a for a in n if a!=' ']
x = len(n) - len(m)

print('"'+' '*x+''.join(m)+'"')