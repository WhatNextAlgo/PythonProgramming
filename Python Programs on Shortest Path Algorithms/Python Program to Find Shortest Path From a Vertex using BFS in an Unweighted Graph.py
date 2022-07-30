from turtle import distance


class Vertex:
    def __init__(self,key= None):
        self.key = key
        self.point_to = {}

    
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
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self,key):
        return self.vertices[key]

    def add_edge(self,src,dest,weight=1):
        self.vertices[src].add_neighbour(self.vertices[dest],weight)

    def does_edge_exist(self,src,dest):
        return self.vertices[src].does_it_point_to(self.vertices[dest])

    def __contains__(self,key):
        return key in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def __len__(self):
        return len(self.vertices)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    

def find_shortest_paths(src):
    parent = {src:None}
    distance = {src:0}
    q = Queue()
    visited = set()
    q.enqueue(src)
    visited.add(src)

    while not q.is_empty():
        curr = q.dequeue()
        for dest in curr.get_neighbours():
            if dest not in visited:
                visited.add(dest)
                parent[dest] = curr
                distance[dest] = distance[curr] + 1
                q.enqueue(dest)

    return parent,distance


g = Graph()
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest>')
print('shortest <vertex key>')
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
 
    elif operation == 'shortest':
        key = int(do[1])
        src = g.get_vertex(key)
        parent, distance = find_shortest_paths(src)
 
        print('Path from destination vertices to source vertex {}:'.format(key))
        for v in parent:
            print('Vertex {} (distance {}): '.format(v.get_key(), distance[v]),
                  end='')
            while parent[v] is not None:
                print(v.get_key(), end = ' ')
                v = parent[v]
            print(src.get_key()) # print source vertex
 
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
   
