class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for ast in asteroids:
            if stk and stk[-1] > 0 and ast < 0:
                while stk and stk[-1] > 0 and ast < 0:
                    top = stk[-1]
                    if abs(top) == abs(ast):
                        stk.pop()
                        ast = float(inf)
                        break
                    elif abs(top) > abs(ast):
                        ast = float(inf)
                        break
                    else:
                        stk.pop()
                if ast!= float(inf):
                    stk.append(ast)

            else:
                stk.append(ast)
        
        return stk