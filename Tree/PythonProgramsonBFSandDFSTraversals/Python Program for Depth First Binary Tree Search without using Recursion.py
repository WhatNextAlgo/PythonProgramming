class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []


    def push(self,data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

class BinaryTree:
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right =None

    def set_root(self,key):
        self.key = key

    def insert_left(self,node):
        self.left = node

    def insert_right(self, node):
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

    def preorder_depth_first(self):
        s = Stack()
        s.push(self)
        while not s.is_empty():
            node = s.pop()
            print(node.key,end=' ')
            if node.right is not None:
                s.push(node.right)
            if node.left is not None:
                s.push(node.left)


    
btree = BinaryTree()
 
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
        print('pre-order dfs traversal: ', end='')
        if btree is not None:
            btree.preorder_depth_first()
        print()
 
    elif operation == 'quit':
        break
