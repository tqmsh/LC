from typing import List   
class Solution:  
    def _check(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0 
        return 1 

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirx = [0,0,-1,1]
        diry = [-1,1,0,0]
        inn = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):  
                for i in range(4):
                    nx = x + dirx[i]
                    ny = y + diry[i]
                    if self._check(nx, ny, matrix) and matrix[nx][ny] > matrix[x][y]: inn[nx][ny] += 1  
                            
        q = [[x, y] for x in range(len(matrix)) for y in range(len(matrix[0])) if inn[x][y] == 0] 
        ans = 0
        # 之所以 top sort, 是因为我们想要，当咱们到 v 的时候/ inn[v] = 0 的时候，我们想尽可能的让这个时间来得慢一些，这样就最常路， 
        # i.e. 1->2->3, 1->1.5->2->3, 第一个会让 in[3] -= 1 = 1，让他被最后一个保留算步数
        while q:  
            for _ in range(len(q)):
                x, y = q.pop(0)
                for i in range(4):
                    nx = x + dirx[i]
                    ny = y + diry[i] 
                    if self._check(nx, ny, matrix) and matrix[nx][ny] > matrix[x][y]:
                        inn[nx][ny] -= 1
                        if inn[nx][ny] == 0:
                            q.extend([(nx, ny)])
            ans += 1 # 每一次走 q 就走树的一层
        return ans 
def main():
    solution = Solution()  
    matrix = [[1,2],[3,4]]
    out = solution.longestIncreasingPath(matrix)
    print(out) 

if __name__ == "__main__":
    main()
