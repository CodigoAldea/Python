a= 'restart'
b= ''
for i in a :
    if i in b :
        i = '$'
        b +=i
    else:
        b +=i
print(b)