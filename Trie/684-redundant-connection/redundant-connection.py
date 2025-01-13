class DSU:
    def __init__(self, n):
        self.rank = [0 for _ in range(n)]
        self.parent = [i for i in range(n)]

    def find(self, i):
        if self.parent[i]!=i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)

        if xrep == yrep:
            return True
        
        xrank = self.rank[xrep]
        yrank = self.rank[yrep]

        if xrank <= yrank:
            self.parent[xrep] = yrep
            self.rank[yrep]+=1
        else:
            self.parent[yrep] = xrep
            self.rank[xrep]+=1
        return False
        


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = DSU(len(edges))

        for u , v in edges:
            if graph.union(u-1,v-1):
                return [u,v]