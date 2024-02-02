class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_1 = set()
        hash_2 = set()

        for n in nums:
            if n in hash_1:
                hash_2.add(n)
            else:
                hash_1.add(n)
        
        return list(hash_2)
