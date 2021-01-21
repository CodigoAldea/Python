'''Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4. '''

l = [int(item) for item in input("Enter the list items : ").split()] 

for i in l[0:5]:
    if i == 9:
        print('true')
    