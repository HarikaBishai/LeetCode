class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        if len(arrays) < 2:
            return 0
        maxVal = arrays[0][-1]
        minVal = arrays[0][0]

        out = float('-inf')

        for i in range(1, len(arrays)):
            out = max(abs(maxVal - arrays[i][0]), abs(arrays[i][-1] - minVal), out)
            maxVal = max(maxVal, arrays[i][-1])

            minVal = min(minVal, arrays[i][0])
        
        return out
