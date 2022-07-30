class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None


    def insert_at_beg(self,new_node):
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end =' ')
            curr = curr.next


a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    node = Node(data)
    a_llist.insert_at_beg(node)
 
print('The linked list: ', end = '')
a_llist.display()

        