class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        ROWS = len(image)
        COLS = len(image[0])


        q = deque([(sr, sc)])

        target = image[sr][sc]
        if target == color:
            return image

        image[sr][sc] = color
        while q:

            r, c = q.popleft()
            
            dir = [(-1,0),(1,0),(0,1),(0,-1)]

            for i , j in dir:
                new_r = i+r
                new_c = j+c
                if new_r in range(ROWS) and new_c in range(COLS) and image[new_r][new_c] == target:
                    image[new_r][new_c] = color
                    q.append((new_r, new_c))

        return image