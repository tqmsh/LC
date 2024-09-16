from typing import List

class Solution:  
    def _check(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0   
        return 1

    def _bfs(self, sx, sy, ex, ey, k, grid):  
        dirx = [-1, 0, 1, 0] # up, right, down, left
        diry = [0, 1, 0, -1]
        vis = set()
        q = [(sx, sy, k, 0)]  
        vis.add((sx, sy, k, 0))
        while q:
            now_x, now_y, now_k, now_step = q.pop(0)  
            if now_x == ex and now_y == ey: 
                return now_step

            for i in range(4):
                nxt_x = now_x + dirx[i]
                nxt_y = now_y + diry[i]
                nxt_k = now_k
                nxt_step = now_step + 1 
                if not self._check(nxt_x, nxt_y, grid): continue
                if grid[nxt_x][nxt_y] == 1: # 贪心，枚举最短路径，遇到挡事的，能用则用  
                    if nxt_k: nxt_k -= 1
                    else: continue
                if (nxt_x, nxt_y, nxt_k) in vis: continue 
                q.append((nxt_x, nxt_y, nxt_k, nxt_step))
                vis.add((nxt_x, nxt_y, nxt_k)) 
        return -1

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] == 1: 
            if k: k -= 1
            else: return -1 
        return self._bfs(0, 0, len(grid) - 1, len(grid[0]) - 1, k, grid) 

def main(): 
    solution = Solution() 
    grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]; k = 1
    out = solution.shortestPath(grid, k) 
    print(out)

main()
 