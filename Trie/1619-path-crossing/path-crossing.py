class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coords = set()

        coords.add((0,0))
        last = (0,0)

        mapping = {
            'N' : (0, 1),
            'W' : (-1,0),
            'S' : (0, -1),
            'E' : (1, 0)
        }
        for dir in path:
            last_x, last_y = last
            curr = (last_x + mapping[dir][0], last_y + mapping[dir][1])
            if curr in coords:
                return True
            last = curr
            coords.add(last)

        return False

            
