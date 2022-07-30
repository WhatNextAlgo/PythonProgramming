class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None


    def append(self,data):
        curr = Node(data)
        if self.head is None:
            self.head = curr
            self.last_node = curr
        else:
            self.last_node.next = curr
            self.last_node = curr


    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" --> ")
            curr = curr.next


alist = LinkedList()
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.display()