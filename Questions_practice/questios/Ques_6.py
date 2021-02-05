'''Given 2 int values, return True if one is negative and one is positive.
 Except if the parameter "negative" is True, then return True only if both are negative.'''

''' conditions :
        1. a < 0, b < 0 
        2. a < 0, b > 0 
        3. a > 0, b < 0 
    parameter == negative 

Output table:

a   b   negative    result
+   -       F           T
-   +       F           T
-   -       T           T
-   -       F           F

'''
a = int(input('enter number : '))
b = int(input('enter number : '))
 #n = 'negative'
negative = True
def p_n(negative, a, b):
    if negative:
        print('true')
    elif :
        print('true')
    else:
        print('false')