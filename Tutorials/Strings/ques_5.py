'''Write a Python program that accepts a comma separated sequence of words as input 
and prints the unique words in sorted form'''

n=input('Enter comma separtaed sequence :')
m=[m for m in n.split(',')]
#print(n)
#print(m)
print(",".join(sorted(list(set(m)))))