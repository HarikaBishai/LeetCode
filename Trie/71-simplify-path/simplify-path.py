class Solution:
    def simplifyPath(self, path: str) -> str:
        out = []

        path = path.split("/")

        for dir in path:
            if dir == '' or dir == '.':
                continue
            if dir == '..' and out:
                out.pop()
            elif dir!='..':
                out.append(dir)
        return "/" + "/".join(out)
            