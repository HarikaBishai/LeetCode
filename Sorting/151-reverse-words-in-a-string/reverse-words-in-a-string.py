class Solution:
    def reverseWords(self, s: str) -> str:
        out = ''
        cnt = 0
        start = 0
        for i, c in enumerate(s+ " "):
            if c == " ":
                curr = s[start: i]
                if curr:
                    if not out:
                        out = s[start: i]
                    else:
                        out = s[start: i] + ' ' + out
                start = i+1
        return out