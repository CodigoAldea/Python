'''Write a Python program to remove the nth index character from a nonempty string.'''

a = input(' Enter the String :')
n = int(input('Enter the index :'))
m =''
for i in range(len(a)):
    if i != n:
        m+=a[i]
print('Required string : ',m)