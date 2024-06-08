class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for src, dest in edges:
            graph[src].append(dest)

        res = 0
        visit, path = set(), set()

        count = [[0]*26 for _ in range(len(colors))]

        def dfs(node):
            if node in path:
                return float('inf')
            if node in visit:
                return 0
            
            visit.add(node)
            path.add(node)

            colorIndex = ord(colors[node]) - ord('a')
            count[node][colorIndex] = 1


            for nei in graph[node]:

                if dfs(nei) == float('inf'):
                    return float('inf')
                for c in range(26):

                    count[node][c] = max(count[node][c], (1 if colorIndex == c else 0) +  count[nei][c])
            
            path.remove(node)
            return max(count[node])




        
        for i in range(len(colors)):
            res = max(res, dfs(i))

        return -1 if res == float('inf') else res
            