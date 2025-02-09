class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return heights
        n = len(heights)
        max_so_far = heights[-1]
        out = [n-1]

        for i in range(n-2, -1, -1):
            if heights[i] > max_so_far:
                out.append(i)
                max_so_far = heights[i]
            

        return out[::-1]