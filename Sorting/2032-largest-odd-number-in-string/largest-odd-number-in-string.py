class Solution:
    def largestOddNumber(self, num: str) -> str:
        rightOdd = -1
        for i in range(len(num)-1, -1, -1):
            if int(num[i])%2 != 0:
                rightOdd = i
                break
        return "" if rightOdd == -1 else num[0:rightOdd+1]
            