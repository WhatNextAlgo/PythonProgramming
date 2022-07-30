class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last_node = self.head

        else:
            self.last_node.next = new_node
            self.last_node = self.last_node.next

    def get_prev_node(self,ref_node):
        curr = self.head
        while (curr and curr.next != ref_node):
            curr = curr.next
        return curr

    def remove(self,ref_node):
        prev_node = self.get_prev_node(ref_node)
        if prev_node is None:
            self.head = ref_node.next
        else:
            prev_node.next = ref_node.next

    
    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end=' ')
            curr = curr.next


def remove_duplicates(llist):
    curr1 = llist.head
    if curr1 is None:
        return None
    while curr1:
        curr2 = curr1.next
        data = curr1.data
        while curr2:
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

            
