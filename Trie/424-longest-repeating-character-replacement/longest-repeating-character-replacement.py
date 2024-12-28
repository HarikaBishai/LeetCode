class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        maxLen = 0

        l = 0

        maxf = 0
        for r in range(len(s)):
            mp[s[r]]+=1
            maxf = max(maxf, mp[s[r]])
            while r-l+1 - maxf > k:
                mp[s[l]]-=1
                l+=1
            maxLen = max(maxLen, r-l+1)
        return maxLen

