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
            self.last_node= self.last_node.next


    def display(self):
        self.display_helper(self.head)

    def display_helper(self,curr):
        if curr is None:
            return None
        print(curr.data,end =" ")
        self.display_helper(curr.next)



a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
 
print('The linked list: ', end = '')
a_llist.display()