class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def get_prev_node(self,ref_node):
        if self.head is None:
            return None
        if self.head == ref_node:
            return None
        curr = self.head 
        while (curr and curr.next != ref_node):
            curr = curr.next
        return curr

    def insert_at_end(self,new_node):
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def remove(self,node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = node.next
        else:
            prev_node.next = node.next

    def duplicate(self):
        copy = LinkedList()
        curr = self.head
        while curr:
            new_node = Node(curr.data)
            copy.insert_at_end(new_node)
            curr = curr.next

        return copy

    def display(self):
        curr = self.head
        while curr:
            print(curr.data,end=' ')
            curr = curr.next


def remove_duplicates(llist):
    curr1 = llist.head
    while curr1:
        curr2 = curr1.next
        data = curr1.data
        while curr2:
            temp = curr2
            curr2 = curr2.next
            if temp.data == data:
                llist.remove(temp)
        curr1 = curr1.next

def find_union(llist1,llist2):
    if llist1.head is None:
        union = llist2.duplicate()
        remove_duplicates(union)
        return union
    if llist2.head is None:
        union = llist1.duplicate()
        remove_duplicates(union)
        return union

    union = llist1.duplicate()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next

    llist2_copy = llist2.duplicate()
    last_node.next = llist2_copy.head
    remove_duplicates(union)
    return union

def find_intersection(llist1,llist2):
    if (llist1.head is None or llist2.head is None):
        return LinkedList()

    intersection = LinkedList()
    current1 = llist1.head
    while current1:
        current2 = llist2.head
        data = current1.data
        while current2:
            if current2.data == data:
                new_node = Node(data)
                intersection.insert_at_end(new_node)
                break
            current2 = current2.next
        current1 = current1.next
    remove_duplicates(intersection)
    return intersection


a_llist1 = LinkedList()
a_llist2 = LinkedList()
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist1.insert_at_end(node)
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist2.insert_at_end(node)
 
union = find_union(a_llist1, a_llist2)
intersection = find_intersection(a_llist1, a_llist2)
 
print('Their union: ')
union.display()
print()
print('Their intersection: ')
intersection.display()
print()
        

