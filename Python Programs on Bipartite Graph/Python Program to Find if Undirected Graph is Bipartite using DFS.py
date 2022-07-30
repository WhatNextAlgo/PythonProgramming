class Vertex:
    def __init__(self,key):
        self.key = key
        self.point_to = {}

    def get_key(self):
        return self.key

    def get_weight(self,dest):
        return self.point_to[dest]
    
    def add_neighbour(self,dest,weight=1):
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

    def add_edge(self,src,dest,weight = 1):
        self.vertices[src].add_neighbour(self.vertices[dest],weight)

    def does_edge_exist(self,src,dest):
        self.vertices[src].does_it_point_to(self.vertices[dest])

    def add_undirected_edge(self,v1_key,v2_key,weight=1):
        self.add_edge(v1_key,v2_key,weight)
        self.add_edge(v2_key,v1_key,weight)

    def does_undirected_edge_exist(self,v1_key,v2_key):
        return (self.does_edge_exist(v1_key,v2_key)and self.does_edge_exist(v2_key,v1_key))

    def __len__(self):
        return len(self.vertices)

    def __contains__(self,key):
        return key in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())


def is_bipartite(vertex,visited):
    colour = {vertex:0}
    return is_bipartite_helper(vertex,visited,colour)

def is_bipartite_helper(v,visited,colour):
    visited.add(v)
    next_colour = 1 - colour[v]
    for dest in v.get_neighbours():
        if dest not in visited:
            colour[dest] = next_colour
            if not is_bipartite_helper(dest,visited,colour):
                return False
        else:
            if colour[dest] != next_colour:
                return False

    return True

g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <vertex1> <vertex2>')
print('bipartite')
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
            v1 = int(do[2])
            v2 = int(do[3])
            if v1 not in g:
                print('Vertex {} does not exist.'.format(v1))
            elif v2 not in g:
                print('Vertex {} does not exist.'.format(v2))
            else:
                if not g.does_undirected_edge_exist(v1, v2):
                    g.add_undirected_edge(v1, v2)
                else:
                    print('Edge already exists.')
 
    elif operation == 'bipartite':
        bipartite = True
        visited = set()
        for v in g:
            if v not in visited:
                if not is_bipartite(v, visited):
                    bipartite = False
                    break
 
        if bipartite:
            print('Graph is bipartite.')
        else:
            print('Graph is not bipartite.')
 
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