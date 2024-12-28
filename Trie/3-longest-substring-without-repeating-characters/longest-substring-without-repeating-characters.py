class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = {}

        l = 0
        maxLen = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            mp[s[r]] = r
            maxLen = max(r-l+1, maxLen)

        return maxLen


        non_repeat = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in non_repeat:
                non_repeat.remove(s[l])
                l+=1
            
            non_repeat.add(s[r])
            maxLen = max(r-l+1, maxLen)
        return maxLen