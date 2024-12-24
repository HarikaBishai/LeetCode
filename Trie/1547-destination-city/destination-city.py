class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = defaultdict(list)
        allNodes = set()
        for u, v in paths:
            graph[u].append(v)
            allNodes.add(u)
            allNodes.add(v)

        
        for node in allNodes:
            if node not in graph:
                return node

        