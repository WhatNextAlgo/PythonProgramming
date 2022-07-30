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


    def get_node(self,index):
        curr = self.head
        for i in range(index):
            curr = curr.next
            if curr is None:
                return None
        return curr

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next


def has_cycle(llist):
    slow = llist.head
    fast = llist.head
    count = 0
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next
        print("slow",slow.data)
        print("fast",fast.data)
        count += 1
        if slow == fast:
            print(fast.next.data)
            print(slow.next.data)
            print("count :",count)
            return True
    return False

def detect_cycle(llist):
    lst = []
    current = llist.head
    while(current):
        if current in lst:
            return current
            
        else:
            lst.append(current)
            current = current.next
    
    return None
 
 
a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
length = len(data_list)
if length != 0:
    values = '0-' + str(length - 1)
    last_ptr = input('Enter the index [' + values + '] of the node'
                     ' to which you want the last node to point'
                     ' (enter nothing to make it point to None): ').strip()
    if last_ptr == '':
        last_ptr = None
    else:
        last_ptr = a_llist.get_node(int(last_ptr))
        a_llist.last_node.next = last_ptr
 
if detect_cycle(a_llist):
    print('The linked list has a cycle.')
else:
    print('The linked list does not have a cycle.')


