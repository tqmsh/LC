from typing import List 
from collections import defaultdict
import math
class Solution:
    def _T(self, dp, i, j, x): # f(x) 单调递增 
        return max(dp[i][j - x], dp[i - 1][x - 1]) <= max(dp[i][j - (x + 1)], dp[i - 1][(x + 1) - 1])
         
    def _get_seq(self, dp, i, j, path) -> List[int]:
        ans = [] 
        while i > 0 and j > 0:
            min_idx = path[i][j]
            # Log the current state
            print(f"i: {i}, j: {j}, min_idx: {min_idx}, dp[i - 1][min_idx - 1]: {dp[i - 1][min_idx - 1]}, dp[i][j - min_idx]: {dp[i][j - min_idx]}")
            
            if min_idx <= 0 or min_idx > j:
                # Exit if min_idx is out of valid range
                break
            
            # Add the current floor to the answer sequence
            ans.append(min_idx)
            
            # Determine whether we go left or down
            if dp[i - 1][min_idx - 1] >= dp[i][j - min_idx]:
                # We would break, so we move down in the dp table
                i -= 1
                j = min_idx - 1 
            else:
                # We would not break, so we move right in the dp table
                j -= min_idx   
        
        # Add the last floor in case of base case
        if i == 1 and j > 0:
            ans.append(j)
        
        return ans[::-1]  # Reverse the list to get the sequence in the correct order



    
    
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(k + 1)] 
        path = [[0] * (n + 1) for _ in range(k + 1)] 
        # 初始化 
        for j in range(n + 1): dp[1][j] = j # k >= 1

        for i in range(2, k + 1):
            min_idx = 0 
            for j in range(1, n + 1): # n >= 1
                if min_idx < j and not self._T(dp, i, j, min_idx): min_idx += 1 
                dp[i][j] = 1 + max(dp[i - 1][min_idx - 1], dp[i][j - min_idx])
                path[i][j] = min_idx
    
        return dp[k][n], self._get_seq(dp, k, n, path)

        
def main():
    solution = Solution()  
    k = 2; n = 100
    out = solution.superEggDrop(k, n)
    print(out) 

if __name__ == "__main__":
    main()
