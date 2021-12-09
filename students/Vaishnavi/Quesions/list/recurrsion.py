def circularly_identical(list1, list2):
      
    # doubling list
    list3 = list1 * 2
      
    # traversal in twice of list1
    for x in range(0, len(list1)):
        z = 0 
          
        # check if list2 == list1 curcularly 
        for y in range(x, x + len(list1)):
            if list2[z]== list3[y]:
                z+= 1
            else:
                break
              
        # if all n elements are same circularly 
        if z == len(list1):
            return True 
      
    return False
          
  
  
# driver code
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
  
  
# check for list 1 and list 2 
if(circularly_identical(list1, list2)):
    print("Yes")
else:
    print("No")
  
# check for list 2 and list 3 
if(circularly_identical(list2, list3)):
    print ("Yes") 
else:
    print ("No") 