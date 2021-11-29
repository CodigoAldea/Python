
def per(l):
    a = len(l)
    if a == 0 :
        return []
    if a == 1 : 
        return [l]

    x = []

    for i in range(a):
        m = l[i]
        v= l[:i]+l[i+1:]
        for b in per(v):
            x.append([m] + b)
    return x

l= [2, 5]
for i in per(l):
    print(i)