''' 
Insertion Sort: 

To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, 
compare it to the elements before.
Move the greater elements one position up to make space 
for the swapped element.
'''

l = [12, 11, 13, 5, 6]
for i in range(1, len(l)) :
    var = l[i]
    j = i - 1      #index
    while var < l[j] and j >= 0:
        l[j+1] = l[j]
        j = j - 1
    l[j+1] = var