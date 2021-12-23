a = int(input("Input number of rows: "))
b = int(input("Input number of columns: "))

l = [[0 for i in range(b)]  for j in range(a)]

for i in range(a):
    for j in range(b):
        l[i][j]= j*i
print(l)