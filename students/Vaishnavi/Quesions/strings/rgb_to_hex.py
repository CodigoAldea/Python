r , g, b = 220 , 20, 60

a = str(r / 16)
a = a.split('.')
#print (a)
if a[0] == '10' : 
    a[0] = 'A'
if a[0] == '11' : 
    a[0] = 'B'
if a[0] == '12' : 
    a[0] = 'C'
if a[0] == '13' : 
    a[0] = 'D'
if a[0] == '14' : 
    a[0] = 'e'
else: 
    a[0]= a[0]
#print (a[0])
s= '.'+a[1]
c= int(float(s)*16)
if c == 10 : 
    c = 'A'
if c == 11 : 
    c = 'B'
if c == 12 : 
    c = 'C'
if c == 13 : 
    c = 'D'
if c == 14 : 
    c = 'e'
else: 
    c= c
#print(a[0]+str(c))

#G
y = str(g / 16)
y = y.split('.')
#print (y)
if y[0] == '10' : 
    y[0] = 'A'
if y[0] == '11' : 
    y[0] = 'B'
if y[0] == '12' : 
    y[0] = 'C'
if y[0] == '13' : 
    y[0] = 'D'
if y[0] == '14' : 
    y[0] = 'e'
else: 
    y[0]= y[0]
#print (y[0])
t= '.'+y[1]
d= int(float(t)*16)
if d == 10 : 
    d = 'A'
if d == 11 : 
    d = 'B'
if d == 12 : 
    d = 'C'
if d == 13 : 
    d = 'D'
if d == 14 : 
    d = 'e'
else: 
    d= d
#print(a[0]+str(c)+y[0]+str(d))

#B
z = str(b / 16)
z = z.split('.')
#print (z)
if z[0] == '10' : 
    z[0] = 'A'
if z[0] == '11' : 
    z[0] = 'B'
if z[0] == '12' : 
    z[0] = 'C'
if z[0] == '13' : 
    z[0] = 'D'
if z[0] == '14' : 
    z[0] = 'e'
else: 
    z[0]= z[0]
#print (z[0])
u= '.'+z[1]
e= int(float(u)*16)
if e == 10 : 
    e = 'A'
if e == 11 : 
    e = 'B'
if e == 12 : 
    e = 'C'
if e == 13 : 
    e = 'D'
if e == 14 : 
    e = 'e'
else: 
    e= e
print("hex value: #"+a[0]+str(c)+y[0]+str(d)+z[0]+str(e))