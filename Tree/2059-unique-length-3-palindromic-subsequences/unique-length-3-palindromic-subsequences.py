class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3:
            return 0

        mapper = {}
        for i in range(len(s)):
            if s[i] not in mapper:
                mapper[s[i]] = [i]
            else:
                mapper[s[i]].append(i)

        out = 0
        for key in mapper.keys():
            indexes = mapper[key]
            if len(indexes) >=2 and indexes[-1] > indexes[0] + 1:
                out+= len(list(set(s[indexes[0]+1 : indexes[-1]])))
        return out
