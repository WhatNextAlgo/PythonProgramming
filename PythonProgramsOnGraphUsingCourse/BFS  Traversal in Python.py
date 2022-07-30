class Graph:
    def __init__(self,gdict= {}):
        self.gdict = gdict


    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)


    def bfs(self,vertex):
        visited = set()
        queue = [vertex]
        visited.add(vertex)

        while queue:
            deVertex = queue.pop(0)
            print(deVertex,end=' ')
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.add(adjacentVertex)
                    queue.append(adjacentVertex)

customDict = {
    "a" : ["b","c"],
    "b" : ["a","d","e"],
    "c" : ["a","e"],
    "d" : ["b","e","f"],
    "e" : ["d","f"],
    "f" : ["d","e"]
    }
g = Graph(customDict)
g.bfs("a")
            