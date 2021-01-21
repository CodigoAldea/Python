'''Given 2 strings, a and b, return the number of the positions where they 
contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, 
since the "xx", "aa", and "az" substrings appear in the same place in both strings.'''


s1 = input('enter string1 : ')
s2 = input('enter string2 : ')

count = 0

small = min(len(s1), len(s2))

for i in range(small):
    s_s1= s1[i:i+2]
    s_s2= s2[i:i+2]
    if s_s1 == s_s2 :
        count = count + 1
print (count)