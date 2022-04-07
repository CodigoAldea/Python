l = [5,3,60,99,10,6,10]
for i in range (len(l)):
    for j in range(len(l)):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
        
print(l)