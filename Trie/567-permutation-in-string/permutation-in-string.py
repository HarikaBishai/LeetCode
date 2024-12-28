class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s2 = {}
        count_s1 = Counter(s1)

        target_s = set()

        l = 0
        for r in range(len(s2)):
            count_s2[s2[r]] = 1 + count_s2.get(s2[r],0)
            if s2[r] in count_s1:
                while count_s2[s2[r]] > count_s1[s2[r]]:
                    count_s2[s2[l]]-=1
                    if count_s2[s2[l]] < count_s1[s2[l]] and s2[l] in target_s:
                        target_s.remove(s2[l])
                    l+=1

                if count_s1[s2[r]] == count_s2[s2[r]]:
                    target_s.add(s2[r])
                if len(target_s) == len(count_s1):
                    return True
            else:
                count_s2 = {}
                target_s = set()
                l = r+1
        return False
            


