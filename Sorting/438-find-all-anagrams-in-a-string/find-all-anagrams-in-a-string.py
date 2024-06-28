class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        target = Counter(p)
        tlen = len(p)

        l = 0
        out = []

        # def check(i):
        #     counter = target.copy()
        #     k = 0
        #     for i in range(i, i+tlen):
        #         if s[i] not in counter or counter[s[i]] == 0:
        #             break
        #         counter[s[i]]-=1
        #         k+=1
        #     return k == tlen

        # for i in range(len(s)-tlen+1):

        #     if check(i):
        #         out.append(i)
        counter= target.copy()
        for i in range(len(s)):
            if s[i] not in p:
                counter= target.copy()
                l = i+1
            else:
                while counter[s[i]] <= 0:
                    counter[s[l]]+=1
                    l+=1
                counter[s[i]]-=1 

                if sum(counter.values()) == 0:
                    out.append(l)





        return out
        

