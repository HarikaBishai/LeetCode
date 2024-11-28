class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        graph = {i+1: set() for i in range(n)}

        for a1, b1 in trust:
            graph[a1].add(b1)
        
        for i in range(1, n+1):
            if graph[i]:
                continue
            flag = True
            for j in range(1, n+1):
                if j != i and i not in graph[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1

            

        