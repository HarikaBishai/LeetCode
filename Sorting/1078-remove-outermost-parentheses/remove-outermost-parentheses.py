class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_count = 0
        close_count = 0
        start = 0
        res = ''

        for i, c in enumerate(s):
            if c == '(':
                open_count+=1
            else:
                close_count+=1
            if open_count == close_count:
                res+=s[start+1:i]
                start=i+1
                open_count = 0
                close_count = 0
        return res