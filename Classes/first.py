str = input('Enter the string : ')
v = [i for i in str if i!=' ']
s = len(str)- len(v)
print( ' '*s +''.join(v))

