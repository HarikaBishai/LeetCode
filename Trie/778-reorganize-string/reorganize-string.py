class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)


        counter
        n = len(s)
        maxHeap = []
        for key, val in counter.items():
            heapq.heappush(maxHeap,(-val, key))

        ans = []

        while maxHeap:
            first_count, first_char = heapq.heappop(maxHeap)

            if not ans or ans[-1] != first_char:
                ans.append(first_char)
                if first_count+1 != 0:
                    heapq.heappush(maxHeap, (first_count+1, first_char))
            elif maxHeap:
                second_count, second_char =  heapq.heappop(maxHeap)
                ans.append(second_char)
                if second_count+1!=0:
                    heapq.heappush(maxHeap, (second_count+1, second_char))
                heapq.heappush(maxHeap, (first_count, first_char))

            else:
                return ""
        return "".join(ans)