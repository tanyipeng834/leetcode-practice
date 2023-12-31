from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        self.height = len(grid)
        self.width = len(grid[0])
        
        for row in range(self.height):
            for col in range(self.width):
                # this represents a rotten orange
                if grid[row][col] == 2:
                    queue.append((col, row, 0))

        def bfs(grid, start_queue):
            visited = set()
            minute = 0  # Initialize minute outside the while loop
            
            while start_queue:
                x, y, minute = start_queue.popleft()
                
                
                # Only visit a fresh orange
                if (x, y) not in visited and  grid[y][x] ==2:
                    visited.add((x, y))
                    # Change the orange to rotten
                   
                    
                    if x - 1 >= 0 and grid[y][x-1]==1:
                        start_queue.append((x - 1, y, minute + 1))
                        grid[y][x-1]= 2

                    if x + 1 < self.width and grid[y][x+1] ==1:
                        start_queue.append((x + 1, y, minute + 1))
                        grid[y][x+1] =2
                    if y - 1 >= 0 and grid[y-1][x] ==1:
                        start_queue.append((x, y - 1, minute + 1))
                        grid[y-1][x] =2
                    if y + 1 < self.height and grid [y+1][x] ==1:
                        start_queue.append((x, y + 1, minute + 1))
                        grid[y+1][x] =2
                        
            
            for row in grid:
                if 1 in row:
                    return -1

            return minute

        return bfs(grid, queue)