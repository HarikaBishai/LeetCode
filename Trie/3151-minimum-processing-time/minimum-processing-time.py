class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        n = len(tasks)
        out = 0
        processorTime.sort(key=lambda x: -x)

        tasks.sort()
        l = 0
        i = 0
        while l < len(tasks):
            if l + 3 < n:
                l = l+3
                out = max(tasks[l]+processorTime[i], out)
                i +=1
            else:
                l = n-1
                out = max(tasks[l]+processorTime[i], out)
                i+=1
            l+=1
        return out