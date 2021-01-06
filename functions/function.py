# adding two numbers 
def add():
    """
    adding two numbers 
    """
    a, b = 2,3
    c= a+ b
    #print(c)
    return c

f= add()
print(f)

def sum(a , b):
    """
    parametarised function for sum of two number
    """
    sum = a+b
    print(sum)

z = 2
y = 5
sum(z, y)


def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return

printinfo( 10 , 20, 50 )
printinfo( 10 )


#sum of 3 numbers 
#multiply by 5 

def sum_of():
    a, b, c = 2, 3 ,5
    d= a+b+c
    return d

x = sum_of()
z = x*5
print (z)


# var = lambda [arg1 [,arg2,.....argn]]:expression


mul = lambda a , b: a*b

print (mul(3,5))