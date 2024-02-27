class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = set()
        maxLength = 0

        l = 0

        for i in range(len(s)):
            char = s[i]
            while char in counter:
                counter.remove(s[l])
                l+=1
            counter.add(char)
            maxLength = max(maxLength, i-l+1)

        return maxLength