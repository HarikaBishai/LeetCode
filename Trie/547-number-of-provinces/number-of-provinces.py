class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*len(isConnected)

        def dfs(city):
            visited[city] = True

            for i in range(len(isConnected)):
                if isConnected[city][i] and not visited[i]:
                    dfs(i)


        cnt = 0
        for city in range(len(isConnected)):
            if not visited[city]:
                cnt+=1
                dfs(city)

        return cnt