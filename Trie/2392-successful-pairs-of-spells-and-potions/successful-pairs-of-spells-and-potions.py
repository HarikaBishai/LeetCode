class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        def getSuccessCount(spell):
            l = 0
            r = len(potions)-1
            ans = -1
            while l<=r:
                m = (l+r)//2
                if potions[m]*spell >= success:
                    r=m-1
                else:
                    l=m+1
            return len(potions) - l
        out = []
        for spell in spells:
            out.append(getSuccessCount(spell))
        return out
            
        