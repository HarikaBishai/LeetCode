class Solution:
    def partitionString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        out = 0
        l=0
        curr = set()
        for r in range(len(s)):
            if s[r] in curr:
                while l < r:
                    curr.remove(s[l])
                    l+=1
                out+=1
            curr.add(s[r])
        return out+1