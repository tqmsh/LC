from typing import List

class Solution:    
    def _check(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0  
        return 1
    
    def _dfs(self, x, y, grid, dp, ans):   
        if dp[x][y]: return 
        
        dp[x][y] = 1 # 初始化
        dirx = [0, 0, -1, 1]
        diry = [-1, 1, 0, 0]

        for i in range(4):
            nx = x + dirx[i]
            ny = y + diry[i] 
            if self._check(nx, ny, grid) and grid[nx][ny] > grid[x][y]: # 不可能倒流，无需 vis/fa
                self._dfs(nx, ny, grid, dp, ans) 
                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
                ans[0] = max(ans[0], dp[x][y]) 

    def longestDecreasingPath(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]  
        ans = [1] # 初始化
        for i in range(len(grid)):
            for j in range(len(grid[0])):  
                self._dfs(i, j, grid, dp, ans) 
        return ans[0]

def main(): 
    solution = Solution() 
    # testCase = [[1,2,3], [1,2,3]]
    testCase = [[1]]
    out = solution.longestDecreasingPath(testCase) 
    print(out) 

if __name__ == "__main__":
    main()
