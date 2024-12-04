class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)


        def isValid(arr):
            if len(set(arr))==1:
                return True
            elif len(arr) == 3:
                start = arr[0]
                i = 1
                while i < 3:
                    curr = arr[i]
                    if start+1 != curr: 
                        return False
                    start = curr
                    i+=1
                return True
            return False

        dp = {len(nums): True}
        def dfs(i):
            if i > n:
                return False
            if i in dp:
                return dp[i]
            
            dp[i] = (i+2 <= n and isValid(nums[i:i+2]) and dfs(i+2)) or (i+3 <= n and isValid(nums[i:i+3]) and dfs(i+3))

            return dp[i]
            
            
        return dfs(0)

        
        

        
        def checkValidity(nums):
            if isValid(nums):
                return True
            for i in range(2, len(nums)):
                if checkValidity(nums[:i]) and checkValidity(nums[i:]):
                    return True
            return False


        return checkValidity(nums)
                