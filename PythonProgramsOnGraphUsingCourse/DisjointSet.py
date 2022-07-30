class DisjoinSet:
    def __init__(self,vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        
        self.rank = dict.fromkeys(vertices,0)

    
    def find(self,item):
        if self.parent[item] != item:
            return self.find(self.parent[item])

        return self.parent[item]

    
    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
            self.rank[yroot] += 1

        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


# vertices = ["A","B","C","D","E"]
# ds= DisjoinSet(vertices)
# ds.union("A","B")
# ds.union("A","C")
# print(ds.find("D"))
