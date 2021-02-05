s = input('Enter a string: ')
d = 0
l = 0
for i in s:
    if i.isdigit():
        d = d+1
    elif i.isalpha():
        l = l+1
    else:
        print('Invalid!!!')

print("Letters", l)
print("Digits", d)