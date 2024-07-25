from collections import defaultdict

class Solution:  
    def _check(self, x, y, grid, vis):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0   
        if (x, y) in vis: return 0
        if grid[x][y] == -1: return 0
        return 1 

    def _bfs(self, sx, sy, ex, ey, grid, e):  
        dirx = [-1, 0, 1, 0]  
        diry = [0, 1, 0, -1]
        vis = set(); vis_tp = set()
        q = [(sx, sy, 0)]  
        vis.add((sx, sy))
        while q: 
            now_x, now_y, now_step = q.pop(0)  
            if now_x == ex and now_y == ey: return now_step

            for i in range(4):
                nxt_x = now_x + dirx[i]
                nxt_y = now_y + diry[i]
                nxt_step = now_step + 1 
                if not self._check(nxt_x, nxt_y, grid, vis): continue
                q.append((nxt_x, nxt_y, nxt_step))
                vis.add((nxt_x, nxt_y)) 

            if grid[now_x][now_y] in vis_tp: continue
            vis_tp.add(grid[now_x][now_y])
            for nxt_y, nxt_y in e[grid[now_x][now_y]]: # 一个传动门必然之用一次，无需回溯，因为以后到这个地方时，肯定没有意义，因为距离变短了
                if (nxt_y, nxt_y) in vis: continue  
                q.append((nxt_x, nxt_y, now_step + 1))
                vis.add((nxt_x, nxt_y))
        
        return -1

    def getMinDistance(self, mazeMap):
        sx = 0; sy = 0; ex = 0; ey = 0; e = defaultdict(list)
        for i in range(len(mazeMap)):
            for j in range(len(mazeMap[0])):
                if mazeMap[i][j] == -2:
                    sx = i; sy = j
                elif mazeMap[i][j] == -3:
                    ex = i; ey = j
                if mazeMap[i][j] > 0:
                    e[mazeMap[i][j]].append((i, j)) 
        return self._bfs(sx, sy, ex, ey, mazeMap, e) 

def main(): 
    solution = Solution() 
    grid = [[1,0,-1,1],[-2,0,-1,-3],[2,2,0,0]]
    # 1, 0, -1, 1
    # -2, 0, -1, -3
    # 2, 2, 0, 0
    out = solution.getMinDistance(grid) 
    print(out)

main()
 
 