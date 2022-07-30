
class Vertex:
    def __init__(self,key):
        self.key = key
        self.point_to = {}

    def get_key(self):
        return self.key
    
    def add_neighbour(self,dest,weight=1):
        self.point_to[dest] = weight

    def get_neighbours(self):
        return self.point_to.keys()

    def get_weight(self,dest):
        return self.point_to[dest]

    def does_it_point_to(self,dest):
        return dest in self.point_to

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

    def get_vertex(self,key):
        return self.vertices[key]

    def add_edge(self,src_key,dest_key,weight=1):
        self.vertices[src_key].add_neighbour(self.vertices[dest_key],weight)

    def does_edge_exist(self,src,dest):
        return self.vertices[src].does_it_point_to(self.vertices[dest])

    def add_undirected_edge(self,v1_key,v2_key,weight=1):
        self.add_edge(v1_key,v2_key,weight)
        self.add_edge(v2_key,v1_key,weight)

    def does_undirected_edge_exist(self,v1_key,v2_key):
        return (self.does_edge_exist(v1_key,v2_key) 
                    and self.does_edge_exist(v2_key,v1_key))

    def __contains__(self,key):
        return key in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())


def label_all_reachable(vertex,component,label):
    return label_all_reachable_helpers(vertex,set(),component,label)

def label_all_reachable_helpers(vertex,visited,component,label):
    visited.add(vertex)
    component[vertex] = label
    for dest in vertex.get_neighbours():
        if dest not in visited:
            label_all_reachable_helpers(dest,visited,component,label)


g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest>')
print('components')
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
                if not g.does_undirected_edge_exist(src, dest):
                    g.add_undirected_edge(src, dest)
                else:
                    print('Edge already exists.')
 
    elif operation == 'components':
        component = dict.fromkeys(g, None)
        label = 1
        for v in g:
            if component[v] is None:
                label_all_reachable(v, component, label)
                label += 1
 
        max_label = label
        for label in range(1, max_label):
            print('Component {}:'.format(label),
                  [v.get_key() for v in component if component[v] == label])
 
 
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
