class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hash = set()
        l = 0
        for i in range(len(nums)):
            while nums[i] in hash:
                if nums[l] == nums[i] and abs(i-l) <= k:
                    return True
                hash.remove(nums[l])
                l+=1

            hash.add(nums[i])
        return False
