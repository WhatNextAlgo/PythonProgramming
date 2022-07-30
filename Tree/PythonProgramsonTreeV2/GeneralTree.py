class Tree:
    def __init__(self,key=None,parent=None):
        self.key = key
        self.children = []
        self.parent = parent


    def add(self,child):
        self.children.append(child)
        child.parent = self


    def set_root(self,key):
        self.key = key

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level = level + 1
            p = p.parent
        return level





    def display(self):
        if self.key is None:
            return
        spaces = 3 * self.get_level() * " " + "|__"
        prefix = spaces if self.parent else ""
        print(prefix +self.key)
        for child in self.children:
            child.display()




tree = Tree()
tree.set_root("Electronics")

laptop = Tree("laptop")
tree.add(laptop)
laptop.add(Tree("MacBook"))
laptop.add(Tree("Microsoft Surface"))
laptop.add(Tree("Thinkpad"))

cellphone = Tree("cellphone")
tree.add(cellphone)
cellphone.add(Tree("Sumsung"))
cellphone.add(Tree("MI"))
cellphone.add(Tree("Realme"))

television = Tree("Televsion")
tree.add(television)
television.add(Tree("LG"))
television.add(Tree("Song"))
television.add(Tree("MI Tv"))

tree.display()
