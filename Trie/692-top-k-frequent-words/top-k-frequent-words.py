class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = {}

        h = []

        for word in words:
            counter[word] = counter.get(word, 0) + 1
        

        for word, count in counter.items():
            heapq.heappush(h, (-count, word))

            

        out = []

        i = 0
        while h and i < k:
            out.append(heapq.heappop(h)[1])
            i+=1
        return out
                
        

        
