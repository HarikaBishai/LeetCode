class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        rank = [1]*n

        components = n

        def find(i):
            if parent[i]==i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(u, v):
            nonlocal components

            urep = find(u)
            vrep = find(v)

            if urep == vrep:
                return
            urank = rank[urep]
            vrank = rank[vrep]

            if urank < vrank:
                parent[urep] = vrep
                rank[vrep] += 1
                components-=1
            else:
                parent[vrep] = urep
                rank[urep] += 1
                components-=1
            return


        for u, v in edges:
            union(u,v)
        return components