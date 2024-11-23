class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        curr = 0
        while n-curr > 0:
            curr+=1
            k+=1
            n-=curr

        return k


        