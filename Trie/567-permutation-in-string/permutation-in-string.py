class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        # counter_s1 = counter(s1)
        s1 = list(s1)
        s1.sort()
        l = 0
        for i in range(len(s2)-n1+1):
            curr = list(s2[i: i+n1])
            curr.sort()
            if s1 == curr:
                return True 
        return False


        
