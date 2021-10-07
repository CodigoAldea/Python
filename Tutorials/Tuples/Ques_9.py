'''Write a Python program to compute element-wise sum of given tuples.'''
t = (1,2,3)
s = (5,6,7)
r = tuple(map(sum, zip(t, s)))
print(r)