'''7 > Write a Python program to count the number 4 in a given list.'''

x= [1, 4, 6, 7, 4, 4, 5 ,6, 8 ,4, 5,4 ]
v = 0
for i in x:
    if i == 4 :
        v =v + 1

print('Number of 4 :', v)