'''Given an List of ints, return the number of 9's in the List.'''

l = [int(item) for item in input("Enter the list items : ").split()] 
count = 0
for i in l:
    if i == 9:
        count = count + 1

print(count)