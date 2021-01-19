'''We have a loud talking parrot. The "hour" parameter is the current hour
time in the range 0..23. We are in trouble if the parrot is talking 
and the hour is before 7 or after 20. Return True if we are in trouble.'''

h = int(input('enter a number between 0 to 23 : '))

if h < 7 or h > 20 :
    print('trouble')
else:
    print(' no trouble')