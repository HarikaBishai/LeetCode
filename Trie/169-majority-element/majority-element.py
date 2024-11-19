class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        Ele =  None

        for n in nums:
            if cnt == 0:
                cnt = 1
                Ele = n
            elif n == Ele:
                cnt+=1
            else:
                cnt-=1

        return Ele