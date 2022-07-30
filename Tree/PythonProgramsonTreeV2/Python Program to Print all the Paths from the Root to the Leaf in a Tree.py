class Tree:
    def __init__(self, data=None):
        self.key = data
        self.children = []
 
    def set_root(self, data):
        self.key = data
 
    def add(self, node):
        self.children.append(node)
 
    def search(self, key):
        if self.key == key:
            return self
        for child in self.children:
            temp = child.search(key)
            if temp is not None:
                return temp
        return None

    def print_all_paths_to_leaf(self):
        self.print_all_paths_to_leaf_helper([]) 


    def print_all_paths_to_leaf_helper(self,path_till_now):
        path_till_now.append(self.key)
        if self.children == []:
            for key in path_till_now:
                print(key, end=' ')
            print()
        else:
            for child in self.children:
                child.print_all_paths_to_leaf_helper(path_till_now[:])



# tree = None
 
# print('Menu (this assumes no duplicate keys)')
# print('add <data> at root')
# print('add <data> below <data>')
# print('paths')
# print('quit')
 
# while True:
#     do = input('What would you like to do? ').split()
 
#     operation = do[0].strip().lower()
#     if operation == 'add':
#         data = int(do[1])
#         new_node = Tree(data)
#         suboperation = do[2].strip().lower() 
#         if suboperation == 'at':
#             tree = new_node
#         elif suboperation == 'below':
#             position = do[3].strip().lower()
#             key = int(position)
#             ref_node = None
#             if tree is not None:
#                 ref_node = tree.search(key)
#             if ref_node is None:
#                 print('No such key.')
#                 continue
#             ref_node.add(new_node)
 
#     elif operation == 'paths':
#         if tree is None:
#             print('Tree is empty.')
#         else:
#             print(tree.print_all_paths_to_leaf())
 
#     elif operation == 'quit':
#         break

lst = [1,2,3,4]
for x in lst:
    print(x)
print(lst[:])


