class Tree:
    def __init__(self,key = None):
        self.key = key
        self.children =[]


    def set_root(self,key):
        self.key = key

    def add(self,node):
        self.children.append(node)


    def search(self,key):
        if self.key == key:
            return self

        for child in self.children:
            temp = child.search(key)
            if temp is not None:
                return temp

        return None



    def sum_nodes(self):
        sum1 = self.key
        for child in self.children:
            sum1 =  sum1 + child.sum_nodes()

        return sum1


tree = None
 
print('Menu (this assumes no duplicate keys)')
print('add <data> at root')
print('add <data> below <data>')
print('sum')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'add':
        data = int(do[1])
        new_node = Tree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            tree = new_node
        elif suboperation == 'below':
            position = do[3].strip().lower()
            key = int(position)
            ref_node = None
            if tree is not None:
                ref_node = tree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            ref_node.add(new_node)
 
    elif operation == 'sum':
        if tree is None:
            print('Tree is empty.')
        else:
            summation = tree.sum_nodes()
            print('Sum of all nodes: {}'.format(summation))
 
    elif operation == 'quit':
        break