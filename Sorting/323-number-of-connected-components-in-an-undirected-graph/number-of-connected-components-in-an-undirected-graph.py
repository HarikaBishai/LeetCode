class UnionFind():
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(0, n)]
        self.rank = [0]*n

    def findParent(self, i):
        if self.parent[i] == i:
            return i
        else:
            topparent = self.findParent(self.parent[i])
            self.parent[i] = topparent
            return topparent
    
    def unionNodes(self, u , v):
        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv:
            return
        
        urank = self.rank[u]
        vrank = self.rank[v]

        if urank < vrank:
            self.parent[pu] = self.parent[pv]
        elif vrank < urank:
            self.parent[pv] = self.parent[pu]
        else:
            self.parent[pu] = self.parent[pv]
            self.rank[pu] += 1

        self.count-=1
class Solution:
   
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u,v in edges:
            uf.unionNodes(u,v)

        return uf.count