class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        graph = defaultdict(list)
        graph[headID] = []
        for employee, manager in enumerate(manager):
            if manager!= -1:
                inform_time = informTime[manager]
                graph[manager].append((employee, inform_time))
        print(graph)


        q = deque([(headID, 0)])
        time = 0

        while q:
            for _ in range(len(q)):
                employee,m_time = q.popleft()
                time = max(time, m_time)

                for nei, nei_time in graph[employee]:
                    q.append((nei, m_time + nei_time))
        return time