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
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next


    def get_node(self,index):
        if self.head is None:
            return None
        curr = self.head
        for x in range(index):
            curr = curr.next

        return curr

    def get_prev_node(self,ref_node):
        if self.head == ref_node:
            return None
        curr = self.head
        while curr.next != ref_node:
            curr = curr.next
        return curr

#1-->2-->3
#2-->3
#1-->1
#2-->1-->3

def interchange(allist,n,m):
    node1 =  allist.get_node(n)
    node2 = allist.get_node(m)
    prev_node1 = allist.get_prev_node(node1)
    prev_node2 = allist.get_prev_node(node2)

    if prev_node1 is not None:
        prev_node1.next = node2
    else:
        allist.head = node2
    
    if prev_node2 is not None:
        prev_node2.next = node1
    else:
        allist.head = node1

    temp = node2.next
    node2.next = node1.next
    node1.next = temp


a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
ans = input('Please enter the two indices of the two elements that'
            ' you want to exchange: ').split()
n = int(ans[0])
m = int(ans[1])
 
interchange(a_llist, n, m)
 
print('The new list: ')
a_llist.display()