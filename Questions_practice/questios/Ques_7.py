'''Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.'''


s = input('enter a string')
s1 = 'not'

if s[:3] == s1 : 
    print(s)
else:
    print(s1+s)