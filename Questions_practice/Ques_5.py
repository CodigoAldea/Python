'''Given an int n, return True if it is within 10 of 100 or 200.'''

a = int(input('enter number : '))

if ((abs(100 - a) <= 10) or (abs(200 - a) <= 10)):
    print('true')
else : 
    print('false')