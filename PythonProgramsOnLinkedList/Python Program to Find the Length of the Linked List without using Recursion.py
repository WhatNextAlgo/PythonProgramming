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


    def length(self):
        curr = self.head
        count = 0
        while curr:
            count = count + 1
            curr = curr.next
        return count
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next


a_llist = LinkedList()
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
print('The length of the linked list is ' + str(a_llist.length()) + '.', end = '')