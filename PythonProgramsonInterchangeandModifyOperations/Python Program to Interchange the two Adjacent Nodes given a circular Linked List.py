class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def get_node(self,index):
        curr = self.head
        for x in range(index):
            curr = curr.next
            if curr == self.head:
                return None
        return curr


    def get_prev_node(self,ref_node):
        curr = self.head
        while curr and curr.next != ref_node:
            curr = curr.next
        return curr

    
    def insert_after(self,ref_node,new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node

    def insert_before(self,ref_node,new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node,new_node)

    def insert_at_end(self,new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            self.insert_before(self.head,new_node)

    def append(self,data):
        self.insert_at_end(Node(data))


    def display(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.head:
                break


def interchange(llist,n):
    current1 = llist.get_node(n)
    current2 = current1.next
    if current2.next != current1:
        before = llist.get_prev_node(current1)
        after = current2.next
        before.next =  current2
        current2.next = current1
        current1.next = after
    
    if llist.head == current1:
        llist.head = current2
    elif llist.head == current2:
        llist.head =current1


a_cllist = CircularLinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_cllist.append(int(data))
 
n = int(input('The nodes at indices n and n+1 will be interchanged.'
              ' Please enter n: '))
 
interchange(a_cllist, n)
 
print('The new list: ')
a_cllist.display()


        
