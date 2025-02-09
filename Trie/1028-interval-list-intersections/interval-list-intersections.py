class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        out = []

        q1 = deque(firstList)
        q2 = deque(secondList)

        while q1 and q2:
            si, ei = q1[0]
            sj, ej = q2[0]

            if sj <= si <= ej or si<= sj<=ei:
                intersection = [max(si, sj), min(ei,ej)]
                out.append(intersection)
            
            if ei<ej:
                q1.popleft()
            else:
                q2.popleft()
                 
            

        return out