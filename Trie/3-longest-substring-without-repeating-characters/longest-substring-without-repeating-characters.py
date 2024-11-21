class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_win = set()
        l = 0
        out = 0
        for r in range(len(s)):
            while s[r] in curr_win:
                curr_win.remove(s[l])
                l+=1
            
            curr_win.add(s[r])
            out = max(out, r-l+1)
        
        return out