from calendar import c


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

    def get_prev_node(self,node):
        curr = self.head
        if curr == node:
            return None
        while curr.next != node:
            curr = curr.next
        return curr

    def remove(self,node):
        prev_node = self.get_prev_node(node)

        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

def remove_duplicates(llist):
    curr1 = llist.head
    while curr1:
        data = curr1.data
        curr2 = curr1.next
        while  curr2:
            if curr2.data == data:
                llist.remove(curr2)
            curr2 = curr2.next
        curr1 = curr1.next

a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
remove_duplicates(a_llist)
 
print('The list with duplicates removed: ')
a_llist.display()    



    

 
    