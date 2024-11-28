class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        graph = {i+1: set() for i in range(n)}


        for a1, b1 in trust:
            graph[a1].add(b1)
        
        
                


        for i in range(1, n+1):
            if graph[i]:
                continue
            j = 1
            flag = True
            while j <= n:
                if j != i:
                    if i not in graph[j]:
                        flag = False
                        break
                j+=1
            if flag:
                return i
        return -1

            

        