#l=[]
k =[]
for i in range(2,50):
    for j in range(2,i):
        if i%j == 0 :
            #k.append(i) # not prime number 
            break
    else:
        k.append(i) # prime number 
        #print ()
print(k)