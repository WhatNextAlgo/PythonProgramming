
class BinaryTree:
    def __init__(self,key=None):
        self.key = key
        self.right = None
        self.left = None

    def set_root(self,key):
        self.key = key

    def insert_left(self,node):
        self.left = node
        
    def insert_right(self,node):
        self.right = node


    def inorder(self):
        if self.left is  not None:
            self.left.inorder()
        print(self.key,end=' ')

        if self.right is not None:
            self.right.inorder()

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


    def print_left_boundary(self):
        if self.left is not None:
            self.left.print_left_boundary()
            print(self.key,end= ' ')
        
        elif self.right is not None:
            self.right.print_left_boundary()
            print(self.key,end= ' ')

        
        
        

    def print_right_boundary(self):
        curr = self
        while True:
            if curr.right is not None:
                print(curr.key,end= ' ')
                curr = curr.right
            elif curr.left is not None:
                print(curr.key,end=' ')
                curr = curr.left
            else:
                break

   

    def print_leaves(self):
        if self.right is not None:
            self.right.print_leaves()
        
        if self.left is not None:
            self.left.print_leaves()

        if self.right is None and self.left is None:
            print(self.key,end=' ')


    def print_border(self):
        print(self.key,end= ' ')
        if self.right is not None:
           self.right.print_right_boundary()
           self.right.print_leaves()
        if self.left is not None:
            self.left.print_leaves()
            self.left.print_left_boundary()







btree = None
 
print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('border')
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
 
    elif operation == 'border':
        if btree is not None:
            print('Border of tree: ')
            btree.print_border()
            print()
    elif operation == 'quit':
        break    
        