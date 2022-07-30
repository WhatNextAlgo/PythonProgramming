class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        
        self.gdict = gdict


    def addEgde(self,vertex,edge):
        self.gdict[vertex].append(edge)


    
customDict = {
    "a" : ["b","c"],
    "b" : ["a","b","e"],
    "c" : ["a","e"],
    "d" : ["b","e","f"],
    "e" : ["d","f"],
    "f" : ["d","e"]
    }

g = Graph(customDict)
print(g.gdict)
g.addEgde("e","c")
print(g.gdict)