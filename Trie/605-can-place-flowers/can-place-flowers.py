class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        


        empty = 0 if flowerbed[0] == 1 else 1

        for f in flowerbed:
            if f:
                n -= int((empty-1)/ 2)
                empty = 0
            else:
                empty+=1
        
        n -= int((empty)// 2)

        return n<=0


        if not n:
            return True
        f = [0] + flowerbed + [0]


        for i in range(1, len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n-=1
            if n == 0:
                return True    
        return False

