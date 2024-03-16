from collections import *
class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        out = []1
        n = len(nums)

        for i in range(n):
            if lower!=nums[i]:
                out.append([lower, nums[i]-1])
            lower = nums[i] + 1
        
        if lower<=upper:
            out.append([lower, upper])

        
            
        return out
    
def main():
    nums = [int(num) for num in  input('Enter the numbers seperated by space: ').split()]
    print(nums)
    lower = int(input('Enter lower: '))
    upper = int(input('Enter upper: '))
    solution = Solution()
    print(solution.findMissingRanges(nums, lower, upper))

if __name__ == '__main__':
    main()