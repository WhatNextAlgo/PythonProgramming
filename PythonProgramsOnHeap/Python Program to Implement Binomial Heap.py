
class BinomialTree:
    def __init__(self,key=None):
        self.key = key
        self.children = []
        self.order = 0

    def add_at_end(self,node):
        self.children.append(node)
        self.order = self.order + 1


class BinomialHeap:
    def __init__(self):
        self.trees = []

    def get_min(self):
        if self.trees == []:
            return None
        least = self.trees[0].key
        for tree in self.trees:
            if tree.key < least:
                least = tree.key
        return least

    def extract_min(self):
        if self.trees == []:
            return None

        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)
        return smallest_node.key


    def combine_roots(self, h):
        self.trees.extend(h.trees)
        self.trees.sort(key = lambda tree: tree.order)

    def merge(self,h):
        self.combine_roots(h)
        if self.trees == []:
            return None
        i =0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if (i + 1 < len(self.trees)-1 and self.trees[i + 2].order == after.order):
                    after_after = self.trees[i + 2]
                    if after.key < after_after.key:
                        after.add_at_end(after_after)
                        del self.trees[i + 2]
                    else:
                        after_after.add_at_end(after)
                        del self.trees[i + 1]

                else:
                    if current.key < after.key:
                        current.add_at_end(after)
                        del self.trees[i + 1]
                    else:
                        after.add_at_end(current)
                        del self.trees[i]
            i = i + 1


    def insert(self,key):
        g = BinomialHeap()
        g.trees.append(BinomialTree(key))
        self.merge(g)

bheap = BinomialHeap()
 
print('Menu')
print('insert <data>')
print('min get')
print('min extract')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        bheap.insert(data)
    elif operation == 'min':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Minimum value: {}'.format(bheap.get_min()))
        elif suboperation == 'extract':
            print('Minimum value removed: {}'.format(bheap.extract_min()))
 
    elif operation == 'quit':
        break