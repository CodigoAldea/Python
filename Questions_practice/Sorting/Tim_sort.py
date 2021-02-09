''' Tim Sort : 

    It's an hybrid sorting algo that uses insertion and merg sort logic.

    Natural RUN : is a sub list which is already ordered.
        * we first start sorting every consecutive set of 32 (i.e minrun)

one type to understanding tim sort :

    - if number of element in the list is < 64 (if the elements is greter than 64 the speed of the insertion 
    sort decreses)
        we use insertion sort 
    else : 
        we make a run (sub list)
            -to make sublist or run we see to the chunk of the element which are either in 
            ascending or decending order. 
            To calculate min_run :
                l = len(list)
                min_run = n 

                such that l/n <= 2**x [x is the power]

        sorting of the run : 
            we use rthe insertion sort to sort the run.
            the sorting is done to get the list sorted in a ascending order.
            
    merging of runs : 
        we merge two adjecent runs, and to do that we use a temporary 
        memory which is equal to the size of the smaller run.

        we use the merg sort. 
        last two level.


second option to understand tim sort : 
    Galloping : 
            l1 = [1, 100, 200, 300]     l2 = [1,2,3,4,5,6,7,8...., 100, 101]

            l = [1, 2,3,4,5,6,7,8, ......., 100 ,100, 200,300]

    
'''

minrun = 32

def InsSort(arr,start,end):    
    for i in range(start+1,end+1):
        elem = arr[i]
        j = i-1
        while j>=start and elem<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = elem
    return arr

def merge(arr,start,mid,end):
    if mid==end:
        return arr
    first = arr[start:mid+1]
    last = arr[mid+1:end+1]
    len1 = mid-start+1
    len2 = end-mid
    ind1 = 0
    ind2 = 0
    ind  = start
     
    while ind1<len1 and ind2<len2:
        if first[ind1]<last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1
     
    while ind1<len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1
              
    while ind2<len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1   
              
    return arr
            

def TimSort(arr):
    n = len(arr)
    
    for start in range(0,n,minrun):
        end = min(start+minrun-1,n-1)
        arr = InsSort(arr,start,end)
        
    curr_size = minrun
    while curr_size<n:    
        for start in range(0,n,curr_size*2):
            mid = min(n-1,start+curr_size-1)
            end = min(n-1,mid+curr_size)
            arr = merge(arr,start,mid,end)
        curr_size *= 2
    return arr


arr = [5, 6, 8, -1, 25, 105, -22, 33]
TimSort(arr)
