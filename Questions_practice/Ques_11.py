''' Given a string, return a new string made of every other char starting 
with the first, so "Hello" yields "Hlo".'''


s = input('enter the string')
t = ''
for i in range(len(s)) : 
    if i % 2 == 0 :
        t = t + s[i]
print(t)