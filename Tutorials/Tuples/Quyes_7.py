'''Write a Python program to calculate the average value of the numbers
 in a given tuple of tuples.'''

t = ((1,4,5), (7,8), (2,4,10))

sum = 0
for s in t:
    for i in s:
        sum = sum + i
res = sum / len(t)
print (res)