from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self,value):
        self.nodes.add(value) 

    def addEdge(self,fromNode,toNode,distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode,toNode)] = distance


def dijkstra(graph,initial):
    visited = {initial:0}
    path = defaultdict(list)
    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node

                elif visited[node] < visited[minNode]:
                    minNode = node

        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight =visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode,edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path


customeGraph = Graph()
customeGraph.addNode("A")
customeGraph.addNode("B")
customeGraph.addNode("C")
customeGraph.addNode("D")
customeGraph.addNode("E")
customeGraph.addNode("F")
customeGraph.addNode("G")
customeGraph.addEdge("A","B",2)
customeGraph.addEdge("A","C",5)
customeGraph.addEdge("B","C",6)
customeGraph.addEdge("B","D",1)
customeGraph.addEdge("B","E",3)
customeGraph.addEdge("C","F",8)
customeGraph.addEdge("D","E",4)
customeGraph.addEdge("E","G",9)
customeGraph.addEdge("F","G",7)

print(dijkstra(customeGraph,"A"))