from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.height = len(maze)
        self.width = len(maze[0])

        def bfs(maze, entrance):
            
            visited= set()
            queue = deque([(entrance[1],entrance[0],0)])
            while queue:
                node = queue.popleft()
                # This is the stopping condition
                x,y ,count = node
            
                if (x,y) not in visited:
                    if (x == 0 or x == self.width -1 or y ==0 or y == self.height -1) and [y,x] != entrance:
                        return count 
                    visited.add((x,y))
                    # Right side Sqaure
                    if x+1<self.width and maze[y][x+1] ==".":
                        queue.append((x+1,y,count+1))
                    # Left side square
                    if x-1 >=0 and maze[y][x-1] ==".":
                        queue.append((x-1,y,count+1))
                    if y-1>=0 and maze[y-1][x] ==".":

                        queue.append((x,y-1,count+1))
                    # Bottom square
                    if y+1<self.height and maze[y+1][x] ==".":
                        queue.append((x,y+1,count+1))
                    
            return -1
        return bfs(maze,entrance)
