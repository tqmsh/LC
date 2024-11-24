from typing import List 
from collections import defaultdict  
from itertools import accumulate
def matrixChainMultiplication(a: List[List[int]]):
        # 区间 dp 模版
        n = len(a); dp = [[0] * n for _ in range(n)]
        # dp[i][j]: [i, j] 合并最小代价
        
        for l in range(2, n): 
            for i in range(1, n - l + 1):  
                j = i + l - 1  
                dp[i][j] = float('inf') # 求 min 调用 inf
                for k in range(i, j): dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + a[i - 1] * a[k] * a[j])
                        
        return dp[1][n - 1]
 
def main():
    arr2 = [1, 2, 3, 4, 3]
    print(matrixChainMultiplication(arr2))

if __name__ == "__main__":
    main()
