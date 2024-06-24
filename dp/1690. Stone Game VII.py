from typing import List 
from collections import defaultdict
import math
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = defaultdict(int); psa = defaultdict(int)  
        for i, stone in enumerate(stones): psa[i] = psa[i - 1] + stone  
 
        for l in range(2, len(stones) + 1): 
            for i in range(len(stones)):  
                j = i + l - 1  
                dp[i, j] = max(psa[j] - psa[i] - dp[i + 1, j], psa[j - 1] - psa[i - 1] - dp[i, j - 1])
 
        return dp[0, len(stones) - 1]
def main():
    solution = Solution()  
    piles = [7,90,5,1,100,10,10,2]
    out = solution.stoneGameVII(piles)
    print(out) 

if __name__ == "__main__":
    main()
