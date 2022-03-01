class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def traverse(self):
        item=self.head
        while item:
            val=item.data
            item=item.next
            yield val
    def append(self,data):
        node=Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head=node
            self.tail=node
        self.count+=1
    def __getitem__(self,i):
        if i > self.count-1:
            return "Index out of range"
        c = self.tail
        for a in range(i):
            c=c.next
        return c.data
obj=linked_list()
obj.append("python")
obj.append("list")
obj.append("tuple")
obj.append("program")
obj.append("set")
print(obj[0])
print(obj[1])