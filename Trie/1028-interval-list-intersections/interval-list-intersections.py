class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        out = []

        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            si, ei = firstList[i]
            sj, ej = secondList[j]

            if sj <= si <= ej or si<= sj<=ei:
                intersection = [max(si, sj), min(ei,ej)]
                out.append(intersection)
            
            if ei<ej:
                i+=1
            else:
                j+=1
                 
            

        return out