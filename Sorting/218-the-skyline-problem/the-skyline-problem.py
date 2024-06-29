class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []

        for i, building in enumerate(buildings):
            edges.append((building[0], i))
            edges.append((building[1], i))

        edges.sort()

        idx = 0
        live, ans = [], []

        while idx < len(edges):
            curr_x = edges[idx][0]

            while idx < len(edges) and curr_x == edges[idx][0]:

                building = buildings[edges[idx][1]]   

                if building[0] == curr_x:
                    heapq.heappush(live, (-building[2], building[1]))


                while live and live[0][1] <= curr_x:
                    heapq.heappop(live)

                idx+=1

            max_height = -live[0][0] if live else 0
            if not ans or ans[-1][1] != max_height:
                ans.append([curr_x, max_height])
        
        return ans