'''Given a non-empty string and an int n, return a new string where the char at index n 
has been removed. The value of n will be a valid index of a char in the original 
string (i.e. n will be in the range 0..len(str)-1 inclusive). '''

s = input('input a string')
i = int(input('input the index'))

#s[i]   s = python i= 3   s[3] = h output = pyton

s1 = s[:i] + s[i+1:]
print(s1)