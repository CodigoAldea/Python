''' How to create a Binary Search Tree '''

class bst():
    def __init__(self, val):
        self.val = val # root node
        self.right = None # RC
        self.left = None #LC

def sort_array(l):
    if not l:
        return None
    mid = len(l)//2
    print("middle index of the array: ",mid)
    print ("the middle element : ",l[mid])
    node = bst(l[mid])
    node.left=sort_array(l[:mid])
    node.right=sort_array(l[mid+1:])
    return node

def output(node):
    if not node:
        return
    print(node.val)
    output(node.left)
    output(node.right)

l = [1,2,3,4,5,6,7]
R = sort_array(l)
output(R)