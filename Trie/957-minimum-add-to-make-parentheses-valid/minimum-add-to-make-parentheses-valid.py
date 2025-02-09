class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        balance = 0

        i = 0
        out = 0
        while i < len(s):
            if s[i] == '(':
                balance+=1
            else:
                if balance:
                    balance-=1
                else:
                    out+=1
            i+=1
        out += balance
        return out
