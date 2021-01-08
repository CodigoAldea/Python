#output


a = 20

# use formatted string literals (f-string)
# f or F 'string'
# variable is inside {}
print(f'the number is {10}')

# str.format()

b = 30 

print('the are ' + '{} ,{}'.format(b , 10) + ' people')

# str() : output : human redable form
# repr() : output : interpreter redable format

# can we print or give output a LIST as a string ? 

f = [2 ,2 ,4 ,5]

for i in range(len(f)):
 print(f'this is a list {f[i]}')

print(f'this is a list {f}')

# number {} = number of arg
# more than two multiplication table : 

a = 3 
b = 4
# range - 1 to 10, for loop
for i in range(1,11):
    #print('{} and {}'.format(a*i,b*i))
    print(str(a*i), repr(b*i))
    #print(repr(b*i))