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


def first_common(llist1,llist2):
    curr1 = llist1.head
    while curr1:
        curr2 = llist2.head
        data = curr1.data
        while curr2:
            if data == curr2.data:
                return data
            curr2 = curr2.next
        curr1 = curr1.next
    return None

llist1 = LinkedList()
llist2 = LinkedList()
 
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))
 
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))
 
common = first_common(llist1, llist2)
 
if common:
    print('The element that appears first in the first linked list that'
          ' is common to both is {}.'.format(common))
else:
    print('The two lists have no common elements.')
