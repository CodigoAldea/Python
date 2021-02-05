'''Given a string, return a new string where the first and last chars have been exchanged.'''


s = input('enter a string : ')

s1 = s[-1] + s[1:-1] + s[0]

print(s1)
