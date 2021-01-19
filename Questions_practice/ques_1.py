#Given two int values, return their sum. 
#Unless the two values are the same, then return double their sum.
def sum(a,b):
    c = a+b
    if a == b:
        c = c*2

    print(c)
    
x = int(input('enter the number:'))
y = int(input('enter the number:'))

sum(x,y)