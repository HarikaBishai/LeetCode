class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        i = 0
        j = 1
        while(i<len(nums)-1):
            

            if nums[i]%2 !=0:

                j = max(j, i+1)

                while(j < len(nums)):
                    if nums[j] %2 == 0:
                        break
                    j+=1
                if j <len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
            i+=1

        return nums


    

