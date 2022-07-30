class Vertex:
    def __init__(self,key=None):
        self.key = key
        self.point_to = {}

    def get_key(self):
        return self.key
    
    def get_weight(self,dest):
        return self.point_to[dest]

    def add_neighbour(self,dest, weight = 1):
        self.point_to[dest] = weight

    def get_neighbours(self):
        return self.point_to

    def does_it_point_to(self,dest):
        return dest in self.point_to

    


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self,key):
        vertex = Vertex(key)
        self.vertices[key] = vertex

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


g = Graph()

print("Menu")
print("add vertex <key>")
print("add edge <src> <dest> <weight> ")
print('display')
print('quit')

while True:
    do = input("What would you like to do? ").split()
    operation = do[0]
    if operation == 'add':
        subopeartion = do[1]
        if subopeartion == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print("Vertex already exists.")
        elif subopeartion == 'edge':
            src = int(do[2])
            dest = int(do[3])
            if src not in g:
                print(f"Vertex {src} does not exist.")
            elif dest not in g:
                print(f"Vertex {dest} does not exist.")
            else:
                if not g.does_edge_exist(src,dest):
                    if len(do) == 5:
                        weight = int(do[4])
                        g.add_edge(src,dest,weight)
                    else:
                        g.add_edge(src,dest)
                else:
                    print('Edge already exists.')

    elif operation == 'display':
        print("Vertex: ",end="")
        for v in g:
            print(v.get_key(),end=" ")
        print()

        print("Edge: ")
        for v in g:
            for des in v.get_neighbours():
                w = v.get_weight(des)
                print(f"(src={v.get_key()}, dest={des.get_key()}, weight={w}) ")
        
        print()
    elif operation == 'quit':
        break

