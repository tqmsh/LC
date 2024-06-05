# Question:
# You are given an m x n binary matrix grid. An island is a group of 1's connected 4-directionally (horizontal or 
# vertical.) Return the maximum area of an island in grid. If there is no island, return 0.

# Input:
# The input is an m x n binary matrix grid where 1 represents land and 0 represents water. Each cell 
# can connect 4-directionally to form an island.

# Output:
# The output is an integer representing the maximum area of an island in the grid, indicating the largest
# number of connected 1's. If there are no islands, the output is 0.
from collections import deque
from typing import List 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 图面积 模版 
        global q, dir, ans, area
        q = deque(); dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]; ans = 0; area = 0

        def check(x, y):
            global q, dir, ans, area
            # 没有越界，没有走过，不是障碍
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0 
            if grid[x][y] != 1: return 0 
            return 1
        
        def bfs():
            global q, dir, ans, area
            while q:
                nowX, nowY = q.popleft()
                # 进队出有很多种情况 - 出队只有一种
                if grid[nowX][nowY] != -1: grid[nowX][nowY] = -1; area += 1
                for d in dir:
                    nxtX, nxtY = nowX + d[0], nowY + d[1]
                    if check(nxtX, nxtY):
                        q.append((nxtX, nxtY))
                        grid[nxtX][nxtY] = -1; area += 1
            return ans
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # 把所有的出发点都放到 q 里面 
                    q.append((i, j))
                    area = 0
                    bfs() 
                    ans = max(ans, area)

        return ans
 
def display_grid(array):
    for row in array:
        for element in row:
            print(f"{element}\t", end="")
        print()  # Newline after each row

def main(): 
    solution = Solution() 
    grid = [[0,0,0,0,0,0,0,0]]
    out = solution.maxAreaOfIsland(grid)
    print(out) 

if __name__ == "__main__":
    main()