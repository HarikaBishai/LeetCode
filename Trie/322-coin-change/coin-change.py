class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        q = deque([0])
        seen = set([0])
        level = 0
        while q:
            for i in range(len(q)):
                start = q.popleft()

                if start == amount:
                    return level

                for coin in coins:
                    if start + coin <= amount and start + coin not in seen:
                        q.append(start+coin)
                        seen.add(start + coin)

            level+=1

        return -1