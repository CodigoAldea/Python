''' How to make a Linked List'''

# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
    
    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next

if __name__=='__main__': 

    first = LinkedList() 

    # creating Node : 
    first.head = Node(1)
    second = Node(2)
    third = Node(3)

    # creating the next:
    first.head.next = second
    second.next = third

    first.printList()
