from typing import List 
from collections import defaultdict
import math
from typing import List

class Solution:
    def _build_x(self, x, data):
        for i in range(len(data)):
            x[i][0] = float('inf'); x[i][1] = -float('inf')
            for j in range(len(data[0])):   
                if data[i][j]: 
                    x[i][0] = min(x[i][0], j)
                    x[i][1] = max(x[i][1], j) 
    def min_steps(self, data: List[List[int]]) -> int:  
        if data == [[]]: return -1 # 🟥 Edge Case: 空 
        dp = [0] * 2; x = [[0] * 2 for _ in range(len(data))] 
        self._build_x(x, data)
        # 初始化
        dp[0] = x[0][0] + 2 * (x[0][1] - x[0][0])
        dp[1] = x[0][1] 
        for i in range(1, len(data)):
            if x[i][0] == float('inf') and x[i][1] == -float('inf'):
                dp[0] += 1; dp[1] += 1
                x[i][0] = x[i - 1][0]; x[i][1] = x[i - 1][1]
            else:
                dp[0] = x[i][1] - x[i][0] + min(dp[1] + abs(x[i - 1][1] - x[i][1]), dp[0] + abs(x[i - 1][0] - x[i][1])) + 1
                dp[1] = x[i][1] - x[i][0] + min(dp[1] + abs(x[i - 1][1] - x[i][0]), dp[0] + abs(x[i - 1][0] - x[i][0])) + 1 
        return min(dp[0], dp[1])

def main():
    solution = Solution()
    data = [[0,1,0,1]]  # Ensure data is a list of lists
    out = solution.min_steps(data)
    print(out)

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
