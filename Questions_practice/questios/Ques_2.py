#Given an int n, return the absolute difference between n and 21, 
#except return double the absolute difference if n is over 21.

y = int(input('enter a number:'))

def a_d(n):
    if n <= 21 :
        print(21-n)
    else:
        print (2*(n-21))

a_d(y)


n = int(input('enter number: '))
def difference(n):
   if n < 22:
        print (21-n)
   else:
        print(2*(n-21))
    
difference(n)