'''Write a Python program to compute the sum of all the elements of each tuple stored 
    inside a list of tuples.'''

t = [(1, 3), (5, 6, 7), (2, 6)]

r = sum(map(sum, t ))
print(r)