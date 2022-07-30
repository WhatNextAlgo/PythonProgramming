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


    def inorder_nth(self,n):
        return self.inorder_nth_helper(n,[])


    def inorder_nth_helper(self,n,inord):
        if self.left is not None:
            temp  = self.left.inorder_nth_helper(n,inord)
            if temp is not None:
                return temp
        inord.append(self)
        if n == len(inord):
            return self

        if self.right is not None:
            temp = self.right.inorder_nth_helper(n,inord)
            if temp is not None:
                return temp


btree = None
 
print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('inorder <index>')
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
 
    elif operation == 'inorder':
        if btree is not None:
            index = int(do[1].strip().lower())
            node = btree.inorder_nth(index)
            if node is not None:
                print('nth term of inorder traversal: {}'.format(node.key))
            else:
                print('index exceeds maximum possible index.')
        else:
            print('Tree is empty.')
 
    elif operation == 'quit':
        break

        

