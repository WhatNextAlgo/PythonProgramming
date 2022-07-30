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


    def alternate(self):
        self.alternate_helper(self.head)

    def alternate_helper(self,curr):
        if curr is None:
            return None
        print(curr.data, end = " ")
        if curr.next and curr.next.next is not None:
            self.alternate_helper(curr.next.next)






a_llist = LinkedList()
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
print('The alternate nodes of the linked list: ', end = '')
a_llist.alternate()