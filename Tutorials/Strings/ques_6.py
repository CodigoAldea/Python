'''Write a Python function to reverses a string if it's length is a multiple of 4'''

a = input('Enter a string : ')
if len(a)%4 ==0 :
    #print(''.join(reversed(a)))
    print(a[::-1])
else:
    print(a)