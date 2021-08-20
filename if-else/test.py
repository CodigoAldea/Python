''' n+nn+nnn+...nnn...n times :
x = int(input('enter the number : '))
a=0
#a = int(x) + int (x+x) + int(x +x +x)
for i in range (1, x+1):
    a += int(str(x)*i)
print(a)'''
import getpass
print(getpass.getuser())