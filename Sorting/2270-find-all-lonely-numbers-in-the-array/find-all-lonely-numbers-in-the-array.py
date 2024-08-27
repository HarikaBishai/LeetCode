class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:

        counter = defaultdict(int)
        out = []
        for i in range(len(nums)):
            counter[nums[i]]+=1
        for i in nums:
            if counter[i] == 1 and i-1 not in counter and i+1 not in counter:
                out.append(i)
        return out
        