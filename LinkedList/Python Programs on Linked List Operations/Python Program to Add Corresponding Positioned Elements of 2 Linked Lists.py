class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None


    def append(self,data):
        new_node  = Node(data)
        if self.head is None:
            self.head = new_node
            self.last_node= self.head
        else:
            self.last_node.next = new_node
            self.last_node = self.last_node.next


    def display(self):
        curr = self.head 
        while curr:
            print(curr.data,end=' ')
            curr = curr.next


def add_linked_lists(llist1,llist2):
    sum_llist = LinkedList()
    curr1 = llist1.head
    curr2 = llist2.head
    while curr1 and curr2:
        sum_llist.append(curr1.data + curr2.data)
        curr1 = curr1.next
        curr2 = curr2.next
    if curr1 is None:
        while curr2:
            sum_llist.append(curr2.data)
            curr2 = curr2.next

    if curr2 is None:
        while curr1:
            sum_llist.append(curr1.data)
            curr1 = curr1.next 

    return sum_llist

llist1 = LinkedList()
llist2 = LinkedList()
 
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))
 
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))
 
sum_llist = add_linked_lists(llist1, llist2)
 
print('The sum linked list: ', end = '')
sum_llist.display()
