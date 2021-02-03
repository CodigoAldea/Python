''' Selection sorting : 
The selection sort algorithm sorts an array by repeatedly 
finding the minimum element (considering ascending order) 
from unsorted part and putting it at the beginning. 
The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) 
from the unsorted subarray is picked and moved to the sorted subarray. '''

''' 
l = [64 25 12 22 11]; We have to sort this list using selection sort Algo:

Step 1 : Find the min value in l[0:4] and place it at the begining : l[0]
Step 2 : Find the min value in l[1:4] and place it at the begining : l[1]
Step 3 : Find the min value in l[2:4] and place it at the begining : l[2]
Step 4 : Find the min value in l[3:4] and place it at the begining : l[3]

'''

l = [64, 25, 12, 22, 11]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i], l[j]= l[j], l[i]
print(l)