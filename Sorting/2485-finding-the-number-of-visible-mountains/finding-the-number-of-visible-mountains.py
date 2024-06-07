class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        peaks.sort(key=lambda x: (x[0] - x[1], -(x[0]+x[1])))


        visible_count = 0
        max_right_so_far = float('-inf')
        prev_peak = None

        for i,x in enumerate(peaks):
            left = x[0]-x[1]
            right = x[0]+x[1]

            

            if right > max_right_so_far:

                max_right_so_far = right
                if i<len(peaks)-1 and x == peaks[i+1]:
                    continue
                visible_count+=1

           
        return visible_count
