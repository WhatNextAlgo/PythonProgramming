
#get_node, get_prev_node, insert_after, insert_before, insert_at_beg, insert_at_end, remove and display

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None


    def get_node(self,index):
        if self.head is None:
            return None
        curr = self.head
        for _ in range(index):
            if curr is None:
                return None
            curr = curr.next

        return curr

    def get_prev_node(self,ref_node):
        if self.head is None:
            return None

        curr = self.head
        while curr and curr.next != ref_node:
            curr= curr.next
        return curr

    def insert_after(self,ref_node,node):
        if self.head is None:
            return None

        node.next = ref_node.next
        ref_node.next = node

    def insert_before(self,ref_node,node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node,node)

    def insert_at_beg(self,node):
        if self.head is None:
            self.head = node
            self.last_node = self.head
        else:
            node.next = self.head
            self.head = node


    def insert_at_end(self,node):
        if self.head is None:
            self.head = node
            self.last_node = self.head
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node


    def remove(self,node):
        if self.head is None:
            return None

        prev_node = self.get_prev_node(node)
        if prev_node is not None:
            prev_node.next = node.next
        else:
            self.head = self.head.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end= " ")
            curr = curr.next
        

a_llist = LinkedList()
 
print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>') 
print('quit')
 
while True:
    print('The list: ', end = '')
    a_llist.display()
    print()
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
 
    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            if position == 'beg':
                a_llist.insert_at_beg(new_node)
            elif position == 'end':
                a_llist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_llist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_llist.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                a_llist.insert_before(ref_node, new_node)
 
    elif operation == 'remove':
        index = int(do[1])
        node = a_llist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_llist.remove(node)
 
    elif operation == 'quit':
        break