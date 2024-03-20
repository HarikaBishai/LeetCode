class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
        if n == 0:
            return 0
        
        possibilites = k ** n       

        print(possibilites)
        def dfs(s, seen):
            if s[-n:] in seen:
                return
            seen.add(s[-n:])

            if len(seen) == possibilites:
                return s
            for i in range(k):
                max_len = dfs(s+str(i), set(list(seen)))
                # print(max_len)
                if max_len: return max_len    
                
            
        return dfs('0' * n, set())

