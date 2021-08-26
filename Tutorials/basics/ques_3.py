'''3 > Write a Python program that accepts an integer (n) and computes the 
value of :        n+nn+nnn+....+n...n times.'''

x = int(input('Enter the number : '))
a=0
for i in range(1,x+1):
    a += int(str(x)*i)   # a = a + int(str(x)*i)
print('solution : ',a)