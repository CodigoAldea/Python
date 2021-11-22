s = input(' Enter a String : ')
step = 3
u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#n = []
x = []
for i in s :
    if i in u:
        index = u.index(i)
        c = (index + step) % 26
        #n.append(c)
        m = u[c]
        x.append(m)
    elif i in l:
        index = l.index(i)
        c = (index + step) % 26
        #n.append(c)
        m = l[c]
        x.append(m)
print(x)