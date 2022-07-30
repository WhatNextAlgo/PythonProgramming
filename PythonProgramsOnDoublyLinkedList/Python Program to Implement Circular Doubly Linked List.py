class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    
    def get_node(self,index):
        if self.head is None:
            return None
        curr = self.head
        for x  in range(index):
            curr = curr.next
            if curr == self.head:
                return None
        return curr

    def insert_after(self,ref_node,new_node):
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node

    def insert_before(self,ref_node,new_node):
        self.insert_after(ref_node.prev,new_node)

    def insert_at_end(self,new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.head.prev,new_node)


    def insert_at_beg(self,new_node):
        self.insert_at_end(new_node)
        self.head = new_node


    
    def remove(self,node):
        if self.head is None:
            return None
        node.prev.next = node.next
        node.next.prev = node.prev
        if self.head == node:
            self.head = node.next


    def display(self):
        if self.head is None:
            return None
        curr = self.head
        while True:
            print(curr.data,end= " ")
            curr = curr.next
            if curr == self.head:
                break


a_cdllist = CircularDoublyLinkedList()
 
print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>') 
print('quit')
 
while True:
    print('The list: ', end = '')
    a_cdllist.display()
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
                a_cdllist.insert_at_beg(new_node)
            elif position == 'end':
                a_cdllist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_cdllist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_cdllist.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                a_cdllist.insert_before(ref_node, new_node)
 
    elif operation == 'remove':
        index = int(do[1])
        node = a_cdllist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_cdllist.remove(node)
 
    elif operation == 'quit':
        break