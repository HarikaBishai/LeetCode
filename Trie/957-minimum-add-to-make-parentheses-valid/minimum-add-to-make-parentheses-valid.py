class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        out = 0
        for c in s:
            if c == '(':
                balance+=1
            else:
                if balance:
                    balance-=1
                else:
                    out+=1
        out += balance
        return out
