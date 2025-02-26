class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = Counter(s)


        n = len(s)
        max_count = 0
        max_char = ''
        for val, count in counter.items():
            if count > max_count:
                max_count = count
                max_char = val

        if max_count > ((n + 1 )// 2):
            return ''
        ans = ['']*n
        index = 0
        while counter[max_char]:
            ans[index] = max_char
            index+=2
            counter[max_char]-=1

        
        for char, count in counter.items():
            while counter[char]:
                if index >= len(s):
                    index = 1
                ans[index] = char
                counter[char]-=1
                index+=2
        return "".join(ans)





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