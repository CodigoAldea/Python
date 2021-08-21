'''7 > Write a Python program to count the number 4 in a given list.'''

x = [1, 4, 6, 7, 4, 4 ,5 ,6 ,4]
c = 0 
for i in x :
    if i == 4 :
        c = c + 1
print(' total number of 4 :', c)