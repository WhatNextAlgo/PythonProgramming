class Vertex:
    def __init__(self,key):
        self.key = key
        self.point_to = {}

    def get_key(self):
        return self.key

    def get_weight(self,dest):
        return self.point_to[dest]

    def add_neighbour(self,dest,weight = 1):
        self.point_to[dest] = weight

    def get_neighbours(self):
        return self.point_to

    def does_it_point_to(self,dest):
        return dest in self.point_to

    
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self,key):
        return self.vertices[key]

    def add_edge(self,src,dest,weight=1):
        self.vertices[src].add_neighbour(self.vertices[dest],weight)

    def does_edge_exist(self,src,dest):
        self.vertices[src].does_it_point_to(self.vertices[dest])

    def __contains__(self,key):
        return key in self.vertices

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values)


def dfs(v, pre, post):
    dfs_helper(v,set(),pre,post,[0]) 

def dfs_helper(vertex,visited,pre,post,time):

    visited.add(vertex)
    time[0] =time[0] + 1
    pre[vertex] = time[0]
    print(f"Visting...{vertex.get_key()} discovered time ... {time[0]}")
    for dest in vertex.get_neighbours():
        if dest not in visited:
            dfs_helper(dest,visited,pre,post,time)
    
    time[0] = time[0] + 1
    post[vertex] = time[0]
    print('Leaving {}... finished time = {}'.format(vertex.get_key(), time[0]))


    
g = Graph()
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest>')
print('dfs <vertex key>')
print('display')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest)
                else:
                    print('Edge already exists.')
 
    elif operation == 'dfs':
        key = int(do[1])
        print('Depth-first Traversal: ')
        vertex = g.get_vertex(key)
        pre = dict()
        post = dict()
        dfs(vertex, pre, post)
        print()
 
    elif operation == 'display':
        print('Vertices: ', end='')
        for v in g:
            print(v.get_key(), end=' ')
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))
        print()
 
    elif operation == 'quit':
        break