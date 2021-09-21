'''Write a Python program to remove consecutive 
duplicates of a given list.'''

from itertools import groupby
a = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3, 9]

t = [i[0]for i in groupby(a)]

print(t)