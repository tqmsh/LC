from typing import List
from collections import Counter

class Solution: 
    def paper(self, grid: List[int]):
        n = len(grid)
        m = len(grid[0])

        # i idx 2darr 模版
        grid_1_based = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                grid_1_based[i + 1][j + 1] = grid[i][j]
        
        dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(n + m + 1)]

        for i in range(1, n + m + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    if not (1 <= i - j <= m and 1 <= i - k <= m): continue 
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j][k - 1], dp[i - 1][j - 1][k], dp[i - 1][j - 1][k - 1]) + grid_1_based[j][i - j] 
                    if j != k:  
                        dp[i][j][k] += grid_1_based[k][i - k]
        
        return dp[2 * n][n][m]
def main():
    solution = Solution()
    nums = [[0, 3, 9], [2, 8, 5], [5, 7, 0]] 
    out = solution.paper(nums)
    print(out) 

if __name__ == "__main__":
    main()