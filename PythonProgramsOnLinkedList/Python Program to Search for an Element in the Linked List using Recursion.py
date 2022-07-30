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
            self.last_node = self.last_node.next

    def display(self):
        curr = self.head
        while curr is  not None:
            print(curr.data, end ="-->")
            curr = curr.next

    def find_index(self,key):
        return self.find_index_helper(key,0,self.head)

    def find_index_helper(self,key,start,node):

        if node is None:
            return -1

        if node.data == key:
            return start
        else:
            return self.find_index_helper(key,start + 1,node.next)

a_llist = LinkedList()
for data in [3, 5, 0, 10, 7]:
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
print()

key = int(input("What data item would like to search for?: "))

index = a_llist.find_index(key)
if index == -1:
    print(str(key) + ' was not found.')
else:
    print(str(key) + ' is at index ' + str(index) + '.')

        
        

        
