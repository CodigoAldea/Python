''' Write a Python program which accepts a sequence of comma 
separated 4 digit binary numbers as its input and print the numbers 
that are divisible by 5 in a comma separated sequence.'''

l = [item for item in input('Enter binary input: ').split()]
s = []
for i in l:
    x = int(i,2)
    if x % 5 == 0:
        #s.append(x)
        print(x)
        print(i)

