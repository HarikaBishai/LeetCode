class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize: return False

        counter = defaultdict(int)
        for key in hand:
            counter[key]+=1
        
        minHeap = [key  for key in counter.keys()]

        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            for i in range(start, start+groupSize):
                if counter[i]:
                    counter[i]-=1
                    if counter[i] == 0:
                        if minHeap[0] != i:
                            return False
                        else:
                            heapq.heappop(minHeap)
                else:
                    return False
        return True

                