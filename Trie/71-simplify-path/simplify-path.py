class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stk = []

        for s in path:
            if s == '.':
                continue
            elif s == '..':
                if stk: stk.pop()
            else:
                if s:
                    stk.append(s)

        return "/"+"/".join(stk)