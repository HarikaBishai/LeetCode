class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        out = 0

        counter =  set()
        l = 0

        for r in range(len(s)):
            while s[r] in counter:
                counter.remove(s[l])
                l+=1
            counter.add(s[r])
            out = max(out, r-l+1)
        return out
        