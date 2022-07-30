from this import d


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node =None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last_node = self.head
        else:
            self.last_node.next = new_node
            self.last_node = self.last_node.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next





def reverse_llist(llist):
    before = None
    curr = llist.head
    if curr is None:
        return None
    
    after = curr.next
    while after:
        curr.next = before
        before = curr
        curr = after
        after = after.next
    curr.next = before
    llist.head = curr


a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
reverse_llist(a_llist)
 
print('The reversed list: ')
a_llist.display()

