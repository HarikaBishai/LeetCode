class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        counter_s1 = Counter(s1)
        
        matches = 0
        curr = defaultdict(int)
        l=0
        for i in range(len(s2)):
            curr[s2[i]]+=1
            
            if s2[i] in counter_s1 and curr[s2[i]] == counter_s1[s2[i]]:
                matches+=1 
            if i-l+1 > len(s1):
                curr[s2[l]]-=1
                if s2[l] in counter_s1 and curr[s2[l]]+1 == counter_s1[s2[l]]:
                    matches-=1
                l+=1
            if matches == len(counter_s1.keys()):
                return True

            
        return False

