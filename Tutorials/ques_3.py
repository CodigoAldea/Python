'''3 > Write a Python program that accepts an integer (n) and computes the 
value of :        n+nn+nnn+....+n...n times.

n=2  : 2 + 22 =24
n = 3 : 3 + 33 + 333
'''

x = int(input(' Enter the number: '))
a = 0
for i in range (1, x+1) :
    a += int(str(x)*i)
print(a)