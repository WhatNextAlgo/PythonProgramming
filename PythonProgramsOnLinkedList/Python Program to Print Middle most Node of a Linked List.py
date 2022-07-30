import math


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

    def get_length(self):
        count = 0
        curr = self.head
        while curr:
            count = count +1
            curr = curr.next
        return count



    def print_middle(self):
        length = self.get_length()

        curr = self.head
        for x in range((length -1)//2):
            curr = curr.next

        if curr:
            if length % 2 == 0:
                print('The two middle elements are {} and {}.'
                    .format(curr.data, curr.next.data))
            else:
                print('The middle element is {}.'.format(curr.data))
        else:
            print('The list is empty.')
                


a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
a_llist.print_middle()
            

