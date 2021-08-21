'''2 > Write a Python program to accept a filename from the user and
 print the extension of that.'''

file = input('Enter the filename with extention : ')
file_extention = file.split(".")
print('filename :', file_extention[0])
print('Extention :', file_extention[-1])