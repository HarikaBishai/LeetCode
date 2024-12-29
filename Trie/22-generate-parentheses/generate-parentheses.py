class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open = 0
        close = 0


        out = []
        stk = []


        def dfs(open, close, stk):
            if open == n and close == n:
                out.append("".join(stk))
            
            if open < n:
                stk.append('(')
                dfs(open+1, close, stk)
                stk.pop()
            if close < open:
                stk.append(')')
                dfs(open, close+1, stk)
                stk.pop()
                
        dfs(0,0, stk)
        return out