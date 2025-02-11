class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        open = 0
        close = 0
        stk = []
        out = []
        def dfs(open, close, stk):
            if open == close == n:
                out.append("".join(stk))
                return
            if open < n:
                stk.append('(')
                dfs(open+1, close, stk)
                stk.pop()
            if close < open:
                stk.append(')')
                dfs(open, close+1, stk)
                stk.pop()
            return
        dfs(0,0,stk)
        return out