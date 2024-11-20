class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        balance = 0
        result = ''
        for char in s:
            if char == '(':
                if balance>0:
                    result+=char
                balance+=1
            else:
                balance-=1
                if balance>0:
                    result+=char
            
           

        return result