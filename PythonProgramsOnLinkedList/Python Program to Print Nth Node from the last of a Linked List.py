class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head= None
        self.last_node = None


    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next


    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end = " ")
            curr = curr.next


def length(allist):
    count = 0 
    curr = allist.head
    while curr:
        count = count +1
        curr = curr.next

    return count


def return_n_from_last(allist,n):
    l = length(allist)
    curr = allist.head
    for x in range(l-n):
        curr = curr.next

    return curr.data


a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
n = int(input('The nth element from the end will be printed. Please enter n: '))
value = return_n_from_last(a_llist, n)
 
print('The nth element from the end: {}'.format(value))


