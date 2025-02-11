class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n-1
        for i in range(n-1, -1, -1):
            if abs(nums[right]) < abs(nums[left]):
                square = nums[left]
                left+=1
            else:
                square = nums[right]
                right-=1
            result[i] = square * square
        return result