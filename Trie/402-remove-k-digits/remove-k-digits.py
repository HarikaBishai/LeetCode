class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num) == k: return "0"
        stk = []

        for val in num:
            while stk and stk[-1] > val and k > 0:
                stk.pop()
                k-=1

            stk.append(val)
        n = len(num)

        s = "".join(stk[:len(stk)-k]).lstrip("0")
        
        return s if s else "0"