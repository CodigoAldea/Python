'''2 > Write a Python program to accept a filename from the user and
 print the extension of that file.'''

 #filename : filename.extention

f = input('Enter the File name : ')
f_e = f.split(".")
print(' File Extention : ', f_e[-1])