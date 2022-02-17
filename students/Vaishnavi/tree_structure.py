'''
        printing a tree like structure from a heap
'''
import heapq
import math
import io


t = 100
last_row = -1
output = io.StringIO()

a = [1,2,3,4,5,6,7,8]
heapq.heapify(a)


for i, n in enumerate(a):
    if i:
        row = int(math.floor(math.log(i+1, 2)))
        print("row = ",row)
    else:
            row = 0

    if row != last_row:
            output.write('\n')
    columns = 2**row
    col_width = int(math.floor((t * 1.0) / columns))
    output.write(str(n).center(col_width, " "))
    print ("last row before = ",last_row)
    last_row = row
    print ("last row = ",last_row)
    print (output.getvalue())
    print ('-' * t)