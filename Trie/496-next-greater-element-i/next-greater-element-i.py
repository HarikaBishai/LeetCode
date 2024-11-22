class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stk = []

        for num in nums2:
            while stk and stk[-1] < num:
                hashmap[stk.pop()] = num
            stk.append(num)

        return [hashmap[num] if num in hashmap  else -1 for num in nums1 ]