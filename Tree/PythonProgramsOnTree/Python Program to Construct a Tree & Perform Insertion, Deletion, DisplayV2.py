class Tree:
    def __init__(self,key=None,parent = None):
        self.key =  key
        self.children = []
        self.parent = parent

    
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

    
    def remove(self,key):
        parent = self.parent
        index  = parent.childern.index(self)
        parent.children.remove(self)
