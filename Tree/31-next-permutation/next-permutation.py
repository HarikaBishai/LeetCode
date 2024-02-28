class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ptr = -1

        for i in range(len(nums)-2, -1, -1):
            if(nums[i]<nums[i+1]):
                ptr=i
                break
        
        if ptr == -1:
            nums[::] = nums[::-1]
            return nums
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i]>nums[ptr]:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                break
            
        nums[ptr+1:] = nums[ptr+1:][::-1]

        return nums
        