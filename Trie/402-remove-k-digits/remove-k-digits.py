class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num) == k:
            return "0"

        stk = []
        i = 0
        for char in num:
            while i < k and stk and int(stk[-1]) > int(char):
                stk.pop()
                i+=1

            if not stk and char == '0':
                continue
            stk.append(char)

        while stk and  i < k:
            stk.pop()
            i+=1
        

        return "0" if not stk else "".join(stk)

        
        