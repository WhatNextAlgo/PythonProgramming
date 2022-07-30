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


    def count(self,key):
        return self.count_helper(self.head,key)

    def count_helper(self,current,key):
        if current is None:
            return 0
        if current.data == key:
            return 1 + self.count_helper(current.next,key)
        else:
            return self.count_helper(current.next,key)
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next


a_llist = LinkedList()
for data in [7, 3, 7, 4, 7, 11, 4, 0, 3, 7]:
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
print()
 
key = int(input('Enter data item: '))
count = a_llist.count(key)
print('{0} occurs {1} time(s) in the list.'.format(key, count))