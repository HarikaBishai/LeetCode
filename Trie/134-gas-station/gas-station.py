class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    
        n = len(gas)
        total_cost = 0
        start = 0
        curr_cost = 0
        for i in range(n):
            total_cost += gas[i] - cost[i]
            curr_cost += gas[i] - cost[i]

            if curr_cost < 0:
                curr_cost = 0
                start = i + 1
        return start if total_cost >=0 else -1
        
        def dfs(curr, bal, start):
            if curr == start:
                return True
            
            bal += gas[curr] - cost[curr]

            if bal >= 0:
                return dfs((curr+1)%n, bal,  start)
        

        for i in range(n):
            if cost[i] <= gas[i] and dfs((i+1)%n, gas[i]-cost[i],  i):
                return i
        return -1



