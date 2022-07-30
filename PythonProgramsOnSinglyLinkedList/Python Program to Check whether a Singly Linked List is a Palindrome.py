class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None
        self.last_node = None


    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head  = new_node
            self.last_node = self.head
        else:
            self.last_node.next = new_node
            self.last_node = self.last_node.next


    def get_prev_node(self,node):
        if self.head is None:
            return None
        curr = self.head
        while curr and curr.next != node:
            curr = curr.next
        return curr
    
    def get_last_node(self):
        if self.head is None:
            return None
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        return curr

    def is_palindrome1(self):
        start = self.head
        end = self.get_last_node()
        print(start.data,end.data)

        while (start != end):# and (end.next != start):
            if start.data != end.data:
                return False

            start = start.next
            end = self.get_prev_node(end)
        return True

def is_palindrome(llist):
    start = llist.head
    end = llist.last_node

    while (start != end):# and (end.next != start):
        if start.data != end.data:
            return False

        start = start.next
        end = llist.get_prev_node(end)
    return True



a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
if is_palindrome(a_llist):
    print('The linked list is palindromic.')
else:
    print('The linked list is not palindromic.')

print(a_llist.is_palindrome1())
