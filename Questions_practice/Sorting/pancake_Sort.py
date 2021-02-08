''' Pancake Sorting 
        - we can perform only 1 logic of flip.
        - we find the greatest element in the list and its index (i)
        and we flip the list from 0 to i
        - now we got the greatest element at l[0]
        - we flip the list from 0 to n(last index), to place the greatest element at the last index. 
        -we do the same till we get the sorted array. 
'''


def flip(arr, i):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
 
# Returns index of the maximum
# element in arr[0..n-1] */
def findMax(arr, n):
    mi = 0
    for i in range(0,n):
        if arr[i] > arr[mi]:
            mi = i
    return mi
 
# The main function that 
# sorts given array 
# using flip operations
def pancakeSort(arr, n):
     
    # Start from the complete
    # array and one by one
    # reduce current size
    # by one
    curr_size = n
    while curr_size > 1:
        # Find index of the maximum
        # element in 
        # arr[0..curr_size-1]
        mi = findMax(arr, curr_size)
 
        # Move the maximum element
        # to end of current array
        # if it's not already at 
        # the end
        if mi != curr_size-1:
            # To move at the end, 
            # first move maximum 
            # number to beginning 
            flip(arr, mi)
 
            # Now move the maximum 
            # number to end by
            # reversing current array
            flip(arr, curr_size-1)
        curr_size -= 1
 
# A utility function to 
# print an array of size n 
def printArray(arr, n):
    for i in range(0,n):
        print ("%d"%( arr[i]),end=" ")
 
# Driver program 
arr = [23, 10, 20, 11, 12, 6, 7]
n = len(arr)
pancakeSort(arr, n)
