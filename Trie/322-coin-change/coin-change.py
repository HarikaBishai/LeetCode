class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        seen = set([0])
        q = deque([(0, 0)])

        while q:
            sum, ncoins = q.popleft()
            if sum == amount:
                return ncoins
            
            for coin in coins:
                if coin + sum <= amount and coin + sum not in seen:
                    q.append(( coin + sum, ncoins+1))
                    seen.add(coin + sum)
        return -1


