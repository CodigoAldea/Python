a = "google.com"
d={}
for i in a :
    if i in d:
        d[i] +=1
    else:
        d[i]=1
print(d)