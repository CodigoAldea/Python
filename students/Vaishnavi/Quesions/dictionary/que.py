from collections import defaultdict
a = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
b = {'x': 300, 'y': 'Red', 'z': 600}

r = defaultdict(list)
for i,j in a.items():
    print (i)
    for x,y in b.items():
        print(x ,y)
        if i == x:
            r[i]= [j,y]
            break
        else:
            r[i]= [j]
print(r)