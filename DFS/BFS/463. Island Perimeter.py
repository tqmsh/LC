
from collections import deque
from typing import List

# Question:
# Given a row x col grid representing a map where grid[i][j] = 1 is land and grid[i][j] = 0 is water,
# determine the perimeter of the island, which is completely surrounded by water and contains no lakes.

# Input:
# The input is a rectangular grid with dimensions not exceeding 100x100, where each cell is either
# land (1) or water (0). The grid represents a single island without any internal water bodies.

# Output:
# The output is an integer representing the perimeter of the island, calculated by counting the
# number of edges forming the boundary of the island cells.
class Solution:   
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 图周长 模版 
        global q, dir, ans
        q = deque(); dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]; ans = 0  

        def check(x, y):
            global q, dir, ans
            # 没有越界，没有走过，不是障碍
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): 
                ans += 1
                return 0
            if grid[x][y] != 1:
                if grid[x][y] == 0: ans += 1 # 空地
                return 0 # -1 走过的土地，不记
            return 1
        
        def bfs():
            global q, dir, ans
            while q:
                nowX, nowY = q.popleft()
                # 进队出有很多种情况 - 出队只有一种
                if grid[nowX][nowY] != -1: grid[nowX][nowY] = -1 
                for d in dir:
                    nxtX, nxtY = nowX + d[0], nowY + d[1]
                    if check(nxtX, nxtY):
                        q.append((nxtX, nxtY))
                        grid[nxtX][nxtY] = -1 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 把所有的出发点都放到 q 里面 
                    q.append((i, j))
                    bfs()
                    return ans
 
def display_grid(array):
    for row in array:
        for element in row:
            print(f"{element}\t", end="")
        print()  # Newline after each row

def main(): 
    solution = Solution()
    # grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] 
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    out = solution.islandPerimeter(grid)
    print(out) 

if __name__ == "__main__":
    main()