''' Radix or bucket sort: 
        We are going to sort the list as per the number or digit in the lasgest number of the list.
           
            say the list is l = [170, 45, 75, 90, 802]
        1.  the largest number is 802.
        2. now we are going to make all the numbers with the same number of digits as 802 (3). 
        3. list will be :
            l = [170, 045, 075, 090, 802]
        4. Now we have to sorth the data using the digit valve i.e we are going to sort the values using the digit value. 

        * number ber of passes will be equal to the number of digit in the largest number in the list.
        
        * It uses counting sort as the subroutine. 

'''



def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i] / exp1) 
        count[int(index % 10)] += 1
  
    # Change count[i] so that count[i] now contains actual 
    # position of this digit in output array 
    for i in range(1, 10): 
        count[i] += count[i - 1] 
  
    # Build the output array 
    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0, len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def radixSort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1 / exp > 0: 
        countingSort(arr, exp) 
        exp *= 10
  
  

arr = [170, 45, 75, 90, 802, 24, 2, 66]  
radixSort(arr) 