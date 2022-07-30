from more_itertools import last


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None


    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.last_node = self.head

        else:
            self.last_node.next = node
            self.last_node = self.last_node.next



def convert_to_circular(llist):
    if llist.last_node:
        llist.last_node.next = llist.head


def print_last_node_points_to(llist):
    last = llist.last_node
    if last is None:
        print('List is empty.')
        return
    
    if last.next is None:
        print('Last node points to None.')
    else:
        print('Last node points to element with data {}.'.format(last.next.data))


a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
print_last_node_points_to(a_llist)
 
print('Converting linked list to a circular linked list...')
convert_to_circular(a_llist)
 
print_last_node_points_to(a_llist)