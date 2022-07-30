class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

#1-->2-->3-->4
#1<--2<--3<--4

def reverse_llist(alist):
    curr = alist.head
    before = None
    if curr is None:
        return None
    after = curr.next
    while after:
        curr.next = before
        before = curr
        print("before: ",before.data)
        curr = after
        after = after.next
    print(curr.data)
    curr.next = before
    alist.head = curr

a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
reverse_llist(a_llist)
 
print('The reversed list: ')
a_llist.display()
