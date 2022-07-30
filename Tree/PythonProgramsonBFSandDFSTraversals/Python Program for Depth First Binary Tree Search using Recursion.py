class BinaryTree:
    def __init__(self,key= None):
        self.key = key
        self.left = None
        self.right = None


    def set_root(self,key):
        self.key = key

    def insert_left(self,node):
        self.left = node

    def insert_right(self,node):
        self.right = node


    def depth_first(self):
        print('entering {}...'.format(self.key))
        if self.left is not None:
            self.left.depth_first()
        print('at {}...'.format(self.key))
        if self.right is not None:
            self.right.depth_first()
        print('leaving {}...'.format(self.key))


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


btree = None
 
print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('dfs')
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
 
    elif operation == 'dfs':
        print('depth-first search traversal:')
        if btree is not None:
            btree.depth_first()
        print()
 
    elif operation == 'quit':
        break

