'''Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in 
the array somewhere. '''

l = [1, 2 ,3, 4,5] 

for i in range (len(l)-2):
    if l[i]==1 and l[i+1]==2 and l[i+2]==3:
        print('true')
else:
    print('false')
