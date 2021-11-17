s = 'hello python {}'
d = 99
a=len(s)
print(s.format(99))
'''# for reading a sequence datatype we use loop
# 1. Index
for i in range(a):
    print(s[i])
# 2. charcter
for i in s:
    print(i)'''
'''
Slicing : 
s[start : stop : step]
@ start is always included
@ stop is never included

print(s[::-1])
r= s.replace("l", "k")
print(r)

Functions : 
upper()
lower()
strip()
replace()
split() :str.split(<symbol>)
format()
'''