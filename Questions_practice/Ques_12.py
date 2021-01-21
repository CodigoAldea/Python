'''Given a non-empty string like "Code" return a string like "CCoCodCode".'''

''' s = code  n = last index of s:  output : s[0] + s[0:2] + s[0:3] + s[0:n+1]'''

s = input('enter the string')
t = ''
r = ''
for i in range(len(s)):
    t = t + s[:i + 1]

for j in range(len(s)+1, 0, -1):
    r = r+ s[:j-1]
print(t + r)


'''
CCoCodCode CodeCodCoC : s[0:n+1] + s[0:n] + .... + s[0]

'''