import heapq
import math
import io


t = 60
last_row = -1
output = io.StringIO()

a = [1,2,3,4,5,6,7,8]
heapq.heapify(a)


for i, n in enumerate(a):
    if i:
        row = int(math.floor(math.log(i+1, 2)))
        #print(row)
    else:
            row = 0
    if row != last_row:
            output.write('\n')
    columns = 2**row
    col_width = int(math.floor((t * 1.0) / columns))
    output.write(str(n).center(col_width, " "))
    last_row = row
    print (output.getvalue())
    print ('-' * t)