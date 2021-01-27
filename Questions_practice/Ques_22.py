'''Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).'''

p = input('enter a string : ')
q = input('enter a string : ')

var =''
big =''
if len(p) > len(q) :
    var = q
    big = p
else :
    var = p
    big = q

print(var + big + var)