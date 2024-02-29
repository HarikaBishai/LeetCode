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

        print(mapper)       
        out = 0
        for key in mapper.keys():
            indexes = mapper[key]
            if len(indexes) >=2 and indexes[-1] > indexes[0] + 1:
                out+= len(list(set(s[indexes[0]+1 : indexes[-1]])))
        return out
        # for l in range(len(s)-2):
        #     r = len(s) - 1
        #     while r > l + 1:
        #         if s[l] == s[r] and s[l] not in visited:
        #             mapper = list(set(s[l+1: r]))
        #             for i in range(len(mapper)):
        #                 new_str = s[l] + "" + mapper[i] + ""+ s[l]
        #                 if  new_str not in palindromes:
        #                     palindromes.add(new_str)
        #             visited.add(s[l])
        #         r-=1
                
        # return len(palindromes)