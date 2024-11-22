class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []

        pairs = list(zip(position, speed))
        pairs.sort(key=lambda x : -x[0])
        for p, s in pairs:
            time = (target - p )/ s
            stk.append(time)
            if stk and len(stk) >=2 and stk[-1] <= stk[-2]:
                stk.pop()
        
        return len(stk)
