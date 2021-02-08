''' Gnome Sorting : 
        1. we move to the 2nd element of the list. 
        2. then we compare the 2nd and 1st element, if the 2nd element is smaller we swap both of them, if not we move to the next element in right. 
        3. Now we will compare the l[2] and l[1] and swap and so on. 
        4 . repeate the process till we reach the end of the list. 
'''

def gnomeSort( arr, n): 
    index = 0
    while index < n: 
        if index == 0: 
            index = index + 1
        if arr[index] >= arr[index - 1]: 
            index = index + 1
        else: 
            arr[index], arr[index-1] = arr[index-1], arr[index] 
            index = index - 1
  
    return arr 
  
arr = [ 34, 2, 10, -9] 
n = len(arr) 
  
arr = gnomeSort(arr, n) 
