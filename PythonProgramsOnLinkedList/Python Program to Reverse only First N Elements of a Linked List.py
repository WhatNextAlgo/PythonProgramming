class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self,data):
        curr = Node(data)
        if self.head is None:
            self.head = curr
            self.last_node = curr
        else:
            self.last_node.next = curr
            self.last_node = self.last_node.next


    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end = "-->")
            curr = curr.next

def reverse_llist(alist,stop,count = 0):
    curr = alist.head
    before = None
    if curr is None:
        return None
    after = curr.next
    while after and count != stop:
        curr.next = before
        before = curr
        curr = after
        after = after.next
        count = count + 1

    alist.head.next = curr
    alist.head = before

a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
n = int(input('Enter the number of elements you want to reverse in the list: '))
 
reverse_llist(a_llist, n)
 
print('The new list: ')
a_llist.display()
