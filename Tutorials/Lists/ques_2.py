'''2. Write a Python program to get a list, sorted in increasing 
order by the last element in each tuple.'''

def last(n):
    return n[-1]
def sort(t):
    return sorted(t, key = last)

a=[(1,3), (3,2), (3,4)]

print(sort(a))