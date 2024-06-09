class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.count = n

    def find(self, i):
        if i == self.parent[i]:
            return i
        else:
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

    def unionNodes(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return

        urank = self.rank[pu]
        vrank = self.rank[pv]

        if urank < vrank:
            self.parent[pu] = pv
        elif urank > vrank:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        self.count -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        UN = UnionFind(n)

        for u, v in edges:
            UN.unionNodes(u, v)

        return UN.count
