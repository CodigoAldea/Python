''' Quick sort :
    take a pivot and compare it with all the elements and divide the list into sub-lists '''

def quick(l):
    low = 0
    high = len(l) - 1
    if low < high :
        p = partition(l)
        quick(l[0:p-1])
        quick(l[p-1:high])

def partition(l):
    low = 0
    high = len(l) - 1
    i = -1
    pivot = l[high]
    for j in range(high):
        if l[j]< pivot:
            i = i+1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[high] = l[high], l[i+1]
    return(i + 1)
l = [10, 80, 30, 90, 40, 50, 70]
quick(l)


