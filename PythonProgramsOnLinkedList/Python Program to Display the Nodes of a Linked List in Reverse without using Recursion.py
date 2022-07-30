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


        
    def display_reversed(self):

        end_node = None
        while end_node != self.head:
            current = self.head        
            while current.next != end_node:
                current = current.next
            print(current.data, end = ' ')
            end_node = current

a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
 
print('The reversed linked list: ', end = '')
a_llist.display_reversed()