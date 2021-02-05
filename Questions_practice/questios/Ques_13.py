'''Given a string, return the count of the number of times that a 
substring length 2 appears in the string and also as the last 2 chars of the string, 
so "hixxxhi" yields 1 (we won't count the end substring). '''

''' s = hi xxx hi b hi x hi   s1: s[0]+s[1] = hi, s[1] + s[2]= ix, xx, xx,  '''

s = input('enter a string : ')

s_l = s[len(s)-2:]
count = 0

for i in range(len(s)-2):
    s1 = s[i:i+2]
    if s1 == s_l:
        count = count + 1
print(count)