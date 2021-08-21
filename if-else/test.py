''' radius of circle 
r = int(input('Enter the Radius :'))
pi = 3.14
a = pi * r**2
print ('area : ',a)
'''
''' file name and extention 
filename= input('Enter the filename : ')
file_ext = filename.split(".")
print(' filename :', file_ext[0])
print(' extention :', file_ext[-1])
'''
''' n+nn+nnn+...nnn...n times :
x = int(input('enter the number : '))
a=0
#a = int(x) + int (x+x) + int(x +x +x)
for i in range (1, x+1):
    a += int(str(x)*i)
print(a)
'''
''' calendar of the given month & year
import calendar
x = int(input('Enter the month :'))
y = int(input('Enter the year : '))
print(calendar.month(y,x))
'''
''' get Current User
import getpass
print(getpass.getuser())
'''
''' Sum of 3 numbers, if the numbers are same return 3 times of there sum. 
a, b, c = [int(x) for x in input(" Enter the number").split()]
sum = a+b+c
if a == b == c:
    print(sum*3)
else:
    print(sum)
'''
'''number of 4's in a list
x= [1, 4, 6, 7, 4,4]
count =0
for i in x:
    if i==4:
        count = count+ 1
print('Number of 4:', count)
'''
''' Letter is vowel or not 
vowels = 'aeiou'
c = input('Enter the charecter : ')
if c in vowels:
    print ('Vowel')
else:
    print('Not Vowel')
'''
'''concatenate all elements in a list into a string and return it.
l = ['hello', 'world', 'have', 'a', 'nice', 'day']
l = ' '.join(l)
print(l)
'''
'''accept the base and height of a triangle and compute the area.
b = int(input('Enter the base : '))
h = int(input('Enter the height : '))
a = b*h/2
print('Area of the Triangle : ', a)
'''