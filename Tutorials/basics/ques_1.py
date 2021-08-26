'''1 > Write a Python program which accepts the radius of a circle from 
the user and compute the area.'''

r = int(input('Enter the Radius :'))
# formula : pi*r^2
pi = 3.14
a = pi * r**2
print('Area : ', a)