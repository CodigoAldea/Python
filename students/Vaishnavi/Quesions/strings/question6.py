s = input(' Enter a String : ')
i = int(input(' Enter the index : '))

if len(s)< i:
    print (" Index out of bound")
else :
    print(s[0:i]+s[i+1:])
    