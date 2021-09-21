'''Write a Python program to generate all sublists of a list.'''

from itertools import combinations
def sub(a):
    s =[]
    for i in range(0, len(a)+1):
        t = [list(x) for x in combinations(a,i)]
        if len(t) >0 :
            s.extend(t)
    return s
a = [1,2,3]
print(sub(a))
