class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        maxElement = max(costs)

        countArray = [0]*(maxElement)

        for ele in costs:
            countArray[ele-1]+=1
        
        counter = 0
        for i in range(len(countArray)):
            if i+1 <= coins:
                while countArray[i] and i+1 <= coins:
                    coins-=i+1
                    countArray[i]-=1
                    counter+=1
            else:
                break
        
        return counter