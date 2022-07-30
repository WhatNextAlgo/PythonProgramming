class Graph:
    def __init__(self,gdict= {}):
        self.gdict = gdict


    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)


    def dfs(self,vertex):
        visited = set()
        stack = [vertex]
        visited.add(vertex)

        while stack:
            popVertex = stack.pop()
            print(popVertex,end=' ')
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.add(adjacentVertex)
                    stack.append(adjacentVertex)
            

customDict = {
    "a" : ["b","c"],
    "b" : ["a","d","e"],
    "c" : ["a","e"],
    "d" : ["b","e","f"],
    "e" : ["d","f"],
    "f" : ["d","e"]
    }
g = Graph(customDict)
g.dfs("a")
            