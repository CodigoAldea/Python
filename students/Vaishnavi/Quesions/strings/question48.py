s = "46a92b45"
v=""
for i in s : 
    if i == "a":
        i = "b"
        v+=i
    elif i == "b":
        i = 'a'
        v+=i
    else:
        v+=i
print(v)