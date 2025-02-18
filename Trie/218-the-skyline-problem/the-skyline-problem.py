class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        positions = []

        for i, building in enumerate(buildings):
            positions.append((building[0], i))
            positions.append((building[1], i))

        positions.sort()
        live = []
        ans = []
        idx = 0

        while idx < len(positions):
            curr_pos = positions[idx][0]
            maxHeight = 0
            while idx < len(positions) and positions[idx][0] == curr_pos:

                b = positions[idx][1]

                building = buildings[b]

                if building[0] == curr_pos:
                    heapq.heappush(live, (-building[2], building[1]))

                while live and live[0][1] <= curr_pos:
                    heapq.heappop(live)
                
                idx+=1
            

            if live :
                maxHeight =  -live[0][0]

            if not ans or ans[-1][1]!=maxHeight:
                ans.append([curr_pos, maxHeight])
        return ans

