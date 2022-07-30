class BinaryTree:
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None

    def set_root(self,key):
        self.key = key


    def insert_left(self,node):
        self.left = node

    def insert_right(self,node):
        self.right = node


    def search(self,key):
        if self.key == key:
            return self

        if self.left is not None:
            temp = self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp = self.right.search(key)
            return temp

        return None

    def inorder_largest(self):
        largest = []
        self.inorder_largest_helper(largest)
        return largest[0]

    def inorder_largest_helper(self,largest):
        if self.left is not None:
            self.left.inorder_largest_helper(largest)
        
        if largest == []:
            largest.append(self.key)
        elif self.key > largest[0]:
            largest[0] = self.key

        if self.right is not None:
            self.right.inorder_largest_helper(largest)
    



btree = None
 
print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('largest')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        new_node = BinaryTree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            btree = new_node
        else:
            position = do[4].strip().lower()
            key = int(position)
            ref_node = None
            if btree is not None:
                ref_node = btree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            if suboperation == 'left':
                ref_node.insert_left(new_node)
            elif suboperation == 'right':
                ref_node.insert_right(new_node)
 
    elif operation == 'largest':
        if btree is None:
            print('Tree is empty.')
        else:
            print('Largest element: {}'.format(btree.inorder_largest()))
 
    elif operation == 'quit':
        break


