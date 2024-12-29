class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(key=lambda x : -x[0])

        
        stk = []
        for pos, sp in zipped:

            time = (target-pos)/sp
            stk.append(time)
            while len(stk) > 1 and  stk[-1] <= stk[-2]:
                stk.pop()
                        
        return len(stk)