class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for num in asteroids:
            if not stk:
                stk.append(num)
                continue
            curr = num
            while stk and stk[-1] > 0 and curr < 0:
                top = stk.pop()
                if abs(top) < abs(num):
                    curr = num
                elif abs(top) > abs(num) :
                    curr = top
                else:
                    curr = None
                    break
            if curr:
                stk.append(curr)
        return stk
                    
               
                