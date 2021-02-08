''' Counting sort : 
        not a comparison sort. 
        we use key to sort. 
        we count elements having different key values. 

        Key : 
            find the largest element which is the key. 

            case : 
                min <= l[i] <= key
            * list should not contain any negative number or value. 
        
        count aray : size = key + 1 , initial value = 0
        it contain the count of the distinct elements. 
'''

def countSort(arr):
    #key = max(arr)
    n = len(arr)
    count = [0]*n
    b = [0] * n

    for i in range(0, n):
        count[arr[i]] += 1
    
    for i in range(n):
        count[i] = count[i] + count[i-1]
    
    i = n - 1
    while i >= 0:
        b[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    print(b)

a = [1, 4, 1, 2, 7, 5, 2, 3, 5, 6, 7, 8, 9, 10]
countSort(a)

