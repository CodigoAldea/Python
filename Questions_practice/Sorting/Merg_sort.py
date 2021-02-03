''' Merg Sort : 
* recurcive by nature .
'''
def merg(l):
    if len(l) > 1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        merg(left)
        merg(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i = i + 1
            else:
                l[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            l[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            l[k] = right[j]
            j = j + 1
            k = k + 1

l = [12, 11, 13, 5, 6, 7]
merg(l)
