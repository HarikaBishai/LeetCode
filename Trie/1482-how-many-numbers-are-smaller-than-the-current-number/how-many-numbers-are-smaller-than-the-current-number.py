class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        temp = sorted(nums)

        mapping = {temp[0]: 0}

        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        
        out = []
        for num in nums:
            out.append(mapping[num])
        
        return out






