class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        res = []
        while l<=r:
            left = nums[l] * nums[l]

            right = nums[r] * nums[r]

            if left > right:
                res.append(left)
                l+=1
            else:
                res.append(right)
                r-=1
        return res[::-1]