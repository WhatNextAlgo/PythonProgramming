
class Node:
    def __init__(self,data):
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

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 


    def get_node(self,index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
            if curr is None:
                return None

        return None


    def get_prev_node(self,ref_node):
        curr = self.head
        while curr and curr.next != ref_node:
            curr = curr.next

        return curr

    def insert_at_beg(self,new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def remove(self,node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = node.next
        else:
            prev_node.next = node.next



def move_even_before_odd(llist):
    curr = llist.head
    while curr:
        temp = curr.next
        if curr.data % 2== 0:
            llist.remove(curr)
            llist.insert_at_beg(curr)
        
        curr = temp

a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
move_even_before_odd(a_llist)
 
print('The new list: ')
a_llist.display()