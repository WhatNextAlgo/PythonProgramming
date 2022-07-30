class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to


def transitive_closure(g):
    """Return dictionary reachable.
 
    reachable[u][v] = True iff there is a path from vertex u to v.
 
    g is a Graph object which can have negative edge weights.
    """
    reachable = {v:dict.fromkeys(g, False) for v in g}
 
    for v in g:
        for n in v.get_neighbours():
            reachable[v][n] = True
 
    for v in g:
         reachable[v][v] = True
 
    for p in g: 
        for v in g:
            for w in g:
                if reachable[v][p] and reachable[p][w]:
                    reachable[v][w] = True
 
    return reachable


g = Graph()
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest>')
print('transitive-closure')
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
 
    elif operation == 'transitive-closure':
        reachable = transitive_closure(g)
        print('All pairs (u, v) such that there is a path from u to v: ')
        for start in g:
            for end in g:
                if reachable[start][end]:
                    print('{}, {}'.format(start.get_key(), end.get_key()))
 
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
 