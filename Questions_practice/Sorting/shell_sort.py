''' Shell sort :

'''


def shell_sort(inp):
    n = len(inp)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = inp[i]
            j = i
            while j >= h and inp[j - h] > t:
                inp[j] = inp[j - h]
                j -= h
 
            inp[j] = t
        h = h // 2
  
inp = [34, 12, 20, 7, 13, 15, 2, 23]
shell_sort(inp)
#print(inp)
