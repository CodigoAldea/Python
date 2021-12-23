def func_name(a= 5) : # function defining 
    print("hello",a )

func_name() # function calling ; passing the arguments (args) 
#parameter key word argument  = (kwargs)

'''
Arbitrary Arguments, *args
def func_name(*a) :
    print("hello",a )

func_name(5,7,9)
Recieved the values of multiple args as a tuple.

Arbitrary Keyword Arguments, **kwargs

def func_name(**a) :
    print("hello",a )

func_name(c = 5, b = 66, d = 77)
we will recieve all the values as  a dict.
'''
