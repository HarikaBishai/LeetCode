class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]

        rank = [1]*(n+1)


        def find(i):
            if parent[i]==i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(u, v):

            urep = find(u)
            vrep = find(v)

            if urep == vrep:
                return False
            urank = rank[urep]
            vrank = rank[vrep]

            if urank < vrank:
                parent[urep] = vrep
                rank[vrep] += 1
            else:
                parent[vrep] = urep
                rank[urep] += 1
            return True


        for u, v in edges:
            if not union(u,v):
                return [u,v]
        return []
