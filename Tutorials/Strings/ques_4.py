'''Write a Python program to remove the characters which have odd index values of a given string.'''

a = input('Enter the String : ')
m=''
for i in range(len(a)):
    if i%2 ==0:
        m+=a[i]
print('New String: ',m)