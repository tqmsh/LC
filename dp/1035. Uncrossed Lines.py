from typing import List 
from collections import defaultdict
import math
class Solution:
    def maxUncrossedLines(self, s: List[int], p: List[int]) -> int:   
        s = [0] + s
        p = [0] + p
        dp = [[0] * len(p) for _ in range(len(s))]

        # Fill the dp table
        for i in range(1, len(s)):
            for j in range(1, len(p)): 
                if s[i] == p[j]: 
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[len(s) - 1][len(p) - 1]
    
def main():
    solution = Solution()  
    nums1 = [1,4,2]; nums2 = [1,2,4]
    out = solution.maxUncrossedLines(nums1, nums2)
    print(out) 

if __name__ == "__main__":
    main()
