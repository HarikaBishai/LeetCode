from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_set = defaultdict(int)
        l, max_length = 0, 0

        for r in range(len(s)):
            if not s[r] in char_set:
                while len(char_set) == 2:
                    char_set[s[l]]-=1
                    if char_set[s[l]] <= 0:
                       char_set.pop(s[l])
                    l+=1     
            char_set[s[r]] +=1
            max_length = max(max_length, r-l+1)

        return max_length