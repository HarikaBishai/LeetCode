class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        dp = [float('inf')]*n
        dp[src] = 0

        for i in range(k+1):
            new_dp = dp.copy()

            for u, v , w in flights:
                if dp[u] != float('inf') and dp[u]+w < new_dp[v]:
                    new_dp[v] = dp[u]+w
            dp = new_dp

        return -1 if dp[dst] == float('inf') else dp[dst]