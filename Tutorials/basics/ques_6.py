'''6 > Write a Python program to calculate the given numbers, 
if the numbers are equal then return three times of their sum.'''

a, b, c = [int(x) for x in input('Enter the Numbers :').split()]
sum = a + b + c
if a == b == c :
    print(sum*3)
else :
    print(sum)