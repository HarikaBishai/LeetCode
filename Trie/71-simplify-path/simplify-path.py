class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")


        stk = []


        for p in path:
            if not p or p == ".":
                continue
            if p == "..":
                if stk: stk.pop()
            else:
                stk.append(p)

        return "/" + "/".join(stk)
