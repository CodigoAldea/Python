''' Coctail Shaker Sort:
        Each iteration of the algorithm is broken up into 2 stages: 
            The first stage loops through the array from left to right, just like the Bubble Sort. 
            During the loop, adjacent items are compared and if value on the left is greater than the value on the right, then values are swapped. 
            At the end of first iteration, largest number will reside at the end of the array.
            The second stage loops through the array in opposite direction- starting from the item just before the most recently sorted item, 
            and moving back to the start of the array. Here also, adjacent items are compared and are swapped if required.    

'''


def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
 
        
        swapped = False
 
        
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
 
        
        if (swapped == False):
            break
 
        
        swapped = False
 
        
        end = end-1
 
        
        for i in range(end-1, start-1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
 
        
        start = start + 1
 
a = [5, 1, 4, 2, 8, 0, 2]
cocktailSort(a)
