from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int)
        
        l, total, res = 0, 0, 0
        
        for r in range(len(fruits)):
            counter[fruits[r]]+=1
            total+=1
            while len(counter) > 2:
                f = fruits[l]
                counter[f]-=1
                total-=1
                l+=1
                if counter[f] == 0:
                    counter.pop(f)
                    
            res = max(res, total)
        return res