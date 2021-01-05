# Example 1


# Ex 2 : Using range(1,101), make two list, 
# one containing all even numbers and other containing 
# all odd numbers.
even = []
odd =[]
for i in range(1,101):
    if i%2 == 0:
        even.append(i)
     
    else:
        odd.append(i)

#From the two list obtained in previous question, 
#make new lists, containing only numbers which are 
#divisible 
#by 4, 6, 9 in separate lists.

four_even = []
four_odd = []

for i in even:
    if i%4 == 0:
        four_even.append(i)
for i in odd:
    if i%4 == 0:
        four_odd.append(i)