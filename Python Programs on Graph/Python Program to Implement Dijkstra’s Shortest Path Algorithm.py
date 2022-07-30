class Vertex:
    def __init__(self,key=None):
        self.key = key
        self.point_to={}

    def get_key(self):
        return self.key

    def add_neighbour(self,dest,weight=1):
        self.point_to[dest] = weight

    def get_neighbours(self):
        return self.point_to


    def does_it_point_to(self,dest):
        return dest in self.point_to

    def get_weight(self,dest):
        return self.point_to[dest]


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

    def get_vertex(self,key):
        return self.vertices[key]

    def __contains__(self,key):
        return key in self.vertices

    def add_edge(self,src,dest,weight=1):
        self.vertices[src].add_neighbour(self.vertices[dest],weight)

    def does_edge_exist(self,src,dest):
        self.vertices[src].does_it_point_to(self.vertices[dest])

    def __iter__(self):
        return iter(self.vertices.values())


def dijkstra(g, source):
    """Return distance where distance[v] is min distance from source to v.
 
    This will return a dictionary distance.
 
    g is a Graph object.
    source is a Vertex object in g.
    """
    unvisited = set(g)
    distance = dict.fromkeys(g,float('inf'))
    distance[source] = 0

    while unvisited != set():
        # find vertex with minimum distance
        closest = min(unvisited,key = lambda v:distance[v])
        
        print("closest",closest.key)
         # mark as visited
        unvisited.remove(closest)
        # update distances
        for neighbour  in closest.get_neighbours():
            if neighbour in unvisited:
                print("--",distance[closest],closest.get_weight(neighbour))
                new_distance = distance[closest] + closest.get_weight(neighbour)
                print("distance[neighbour] -- ",neighbour.key,distance[neighbour])
                if distance[neighbour] > new_distance:
                    distance[neighbour] = new_distance


    return distance


g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('shortest <source vertex key>')
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
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                    g.add_edge(dest, src, weight)
                else:
                    print('Edge already exists.')
 
    elif operation == 'shortest':
        key = int(do[1])
        source = g.get_vertex(key)
        distance = dijkstra(g, source)
        print('Distances from {}: '.format(key))
        for v in distance:
            print('Distance to {}: {}'.format(v.get_key(), distance[v]))
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
