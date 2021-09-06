'''Write a Python program to count and display the vowels of a given text.'''

a = input('Enter the text :')
m = 'aeiouAEIOU'
x =''
n = 0
for i in a :
    if i in m:
        x+=i
        n+=1
print('list: ',x, 'count: ', n)