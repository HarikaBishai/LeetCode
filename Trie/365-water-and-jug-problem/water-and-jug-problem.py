class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        
        seen = set([(0,0)])
        q = deque([(0,0)])
        
        while q:
            for _ in range(len(q)):
                j1, j2 = q.popleft()
                if j1+j2 == target:
                    return True


                dir = [(x, j2), (j1, y),(0, j2),(j1, 0),  (min(j1+j2, x), max(j2-j1, 0)), (max(j1-j2, 0), min(y, j1+j2))]
                for i, j in dir:
                    if (i,j) not in seen:
                        q.append((i,j))
                        seen.add((i,j))
            
        return False
        

        