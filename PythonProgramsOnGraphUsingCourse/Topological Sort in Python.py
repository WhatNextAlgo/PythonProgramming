from collections import defaultdict

class Graph:
    def __init__(self,numberOfVertex):
        self.graph = defaultdict(list)
        self.numberOfVertex = numberOfVertex


    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)

    def topological_sort_helper(self,v,visited,stack):
        visited.append(v)
        for adjacentVertex in self.graph[v]:
            if adjacentVertex not in visited:
                self.topological_sort_helper(adjacentVertex,visited,stack)

        stack.insert(0,v)


    def topological_sort(self):
        visited = []
        stack = []
        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_helper(k,visited,stack)

        print(stack)



g = Graph(8)
g.addEdge("A","C")
g.addEdge("C","E")
g.addEdge("E","F")
g.addEdge("F","G")
g.addEdge("E","H")
g.addEdge("B","C")
g.addEdge("B","D")
g.addEdge("D","F")

g.topological_sort()