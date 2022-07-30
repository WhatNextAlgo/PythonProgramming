import DisjointSet as dst

class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])

    def addNode(self,value):
        self.nodes.append(value)

    def print_solution(self):
        for s,d,w in self.MST:
            print(s,' - ',d,':',w)

    
    def kruskalAlgo(self):
        i,e = 0, 0

        ds = dst.DisjoinSet(self.nodes)

        self.graph = sorted(self.graph,key = lambda item:item[2])
        while e < self.v -1:
            s,d,w = self.graph[i]
            i +=1
            x= ds.find(s)
            y = ds.find(d)
            if x != y:
                e +=1
                self.MST.append([s,d,w])
                ds.union(x,y)

        self.print_solution()



g = Graph(5)

g.addNode('A')
g.addNode('B')
g.addNode('C')
g.addNode('D')
g.addNode('E')

g.addEdge("A","B",5)
g.addEdge("B","A",5)
g.addEdge("A","C",13)
g.addEdge("C","A",13)
g.addEdge("A","E",15)
g.addEdge("E","A",15)
g.addEdge("E","C",20)
g.addEdge("C","E",20)
g.addEdge("C","B",10)
g.addEdge("B","C",10)
g.addEdge("C","D",6)
g.addEdge("D","C",6)
g.addEdge("B","D",8)
g.addEdge("B","B",8)

g.kruskalAlgo()


