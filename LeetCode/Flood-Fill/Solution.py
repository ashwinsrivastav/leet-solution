1from collections import deque
2class Solution:
3    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
4        original_color = image[sr][sc]
5        
6        if original_color == color:
7            return image
8        
9        rows, cols = len(image), len(image[0])
10        queue = deque([(sr, sc)])
11        
12        while queue:
13            r, c = queue.popleft()
14            
15            if image[r][c] == original_color:
16                image[r][c] = color
17                if r + 1 < rows:
18                    queue.append((r + 1, c))
19                if r - 1 >= 0:
20                    queue.append((r - 1, c))
21                if c + 1 < cols:
22                    queue.append((r, c + 1))
23                if c - 1 >= 0:
24                    queue.append((r, c - 1))
25        
26        return image