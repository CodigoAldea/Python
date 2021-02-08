''' Bitonic Sort:
        1. make the bitonic sequence (1st half is in ascending order and 2nd hlaf is in descending order)
            a. conpase the consicutive element to find  the min and max values.
            b. conpare the 2nd consitive element to find the nin and max values, and reittrate the step 1. 
            c. we got the Bitonic sequence.
        2. Sort the nitonic list or sequence. 
            a. Now we  have a list whos 1st half is sorte in increasing order and 2nd half is sorted in decreasing order. 
            b. Now we compare the 1st element or the 1st half with the 1st element of 2nd half and so on. 
            c. now we call the bitonic sequence function and get a sorted list.
'''

def compAndSwap(a, i, j, dire): 
    if (dire==1 and a[i] > a[j]) or (dire==0 and a[i] < a[j]): 
        a[i],a[j] = a[j],a[i] 
  
def bitonicMerge(a, low, cnt, dire): 
    if cnt > 1: 
        k = cnt//2
        for i in range(low , low+k): 
            compAndSwap(a, i, i+k, dire) 
        bitonicMerge(a, low, k, dire) 
        bitonicMerge(a, low+k, k, dire) 
  
def bitonicSort(a, low, cnt,dire): 
    if cnt > 1: 
          k = cnt//2
          bitonicSort(a, low, k, 1) 
          bitonicSort(a, low+k, k, 0) 
          bitonicMerge(a, low, cnt, dire) 
  
def sort(a,N, up): 
    bitonicSort(a,0, N, up) 
  
a = [3, 7, 4, 8, 6, 2, 1, 5] 
n = len(a) 
up = 1
  
sort(a, n, up) 
print ("\n\nSorted array is") 
for i in range(n): 
    print("%d" %a[i])
