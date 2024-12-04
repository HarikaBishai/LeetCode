class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        graph = {i+1:[] for i in range(n)}

        indegree = {i+1:0 for i in range(n)}
        for u,v in relations:
            graph[u].append(v)

            indegree[v]+=1

        q = deque()
        finish = 0
        for i in range(n):
            if indegree[i+1] == 0:

                q.append(i+1)
                finish+=1
        
        res = 0
        
        while q:
            

            for i in range(len(q)):
                node = q.popleft()
                
                for nei in graph[node]:
                    indegree[nei]-=1
                    if indegree[nei] == 0:
                        q.append(nei)
                        finish+=1
            res+=1
        print(finish)
        return res if finish == n else -1


        

        