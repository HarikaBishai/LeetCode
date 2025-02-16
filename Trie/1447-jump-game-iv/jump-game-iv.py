class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        graph = {}

        for i, num in enumerate(arr):
            if num in graph:
                graph[num].append(i)
            else:
                graph[num] = [i]

        
        visited = set([0])
        q = deque([0])

        res = 0

        while q:
            for i in range(len(q)):
                index = q.popleft()
                if index == n-1:
                    return res

                for nei in graph[arr[index]]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
                graph[arr[index]].clear()
                for nei in [index-1, index+1]:
                    if nei in range(0, n) and nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            res+=1
        return res

