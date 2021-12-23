b = input ( "Enter the number : ")  # string

a = list(map(int, b)) # to make chnages we need a list 

l = len(b) # length for the index

# Start from the right most digit and find the first digit that is smaller than the digit next to it.
for i in range (l-1, 0 ,-1):
    if a[i]> a[i-1] :
        break

# If no such digit found,then all numbers are in descending order, no greater number is possible.
if i == 1 and a[i] <= a[i-1]:
    print("Next num not possible")

# Find the smallest digit on the right side of (i-1)'th digit that is greater than number[i-1]
x = a[i-1]
small = i
for j in range(i+1, l):
    if a[j]> x and a[j]< a[small]:
        small = j

# Swapping the above found smallest digit with (i-1)'th
a[small], a[i-1] = a[i-1], a[small]

x = 0  # final output

# Converting list upto i-1 into number
for j in range(1):
    x = x*10+a[j]

a= sorted(a[i:]) # sorthing the digits in ascending order

# converting the remaining sorted digits into number
for j in range(l-i):
    x =x*10 + a[j]

print("next number :", x)