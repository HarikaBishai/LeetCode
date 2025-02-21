class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        seen = set([0])
        q = deque([[0, 0]])

        while q:
            sum, n_coins= q.popleft()
            if sum == amount:
                return n_coins
            for coin in coins:
                if coin + sum <= amount and coin + sum not in seen:
                    seen.add(coin + sum)
                    q.append([coin + sum, n_coins+1])
        return -1

        

        

