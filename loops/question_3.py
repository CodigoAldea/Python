#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.

x = int(input('enter the quantity :'))
if x*100 > 1000 :
    print('cost : ', (x*100)-(.1*x*100))
else:
    print('cost : ', x*100)