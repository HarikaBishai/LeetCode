class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        out = []
        stk = []


        def backtrack(open, close):
            if open == close == n:
                out.append("".join(stk))
                return
            
            if open < n:
                stk.append('(')
                backtrack(open+1,close)
                stk.pop()
            if close < open:
                stk.append(')')
                backtrack(open,close+1)
                stk.pop()
        backtrack(0,0)
        return out

