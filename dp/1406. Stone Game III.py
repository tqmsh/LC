from typing import List 
from collections import defaultdict
import math
class Solution:
    def stoneGameIII(self, piles: List[int]) -> int:   
        dp = defaultdict(int)
        sum = 0  
        for i in range(len(piles) - 1, -1, -1): 
            sum += piles[i] # [i, len)
            if i == len(piles) - 1:
                dp[i] = sum
            elif i == len(piles) - 2:
                dp[i] = max(sum - dp[i + 1], sum)
            elif i == len(piles) - 3:
                dp[i] = max(sum - dp[i + 1], sum - dp[i + 2], sum)  
            else: 
                dp[i] = max(sum - dp[i + 1], sum - dp[i + 2], sum - dp[i + 3])
            
        if dp[0] > sum - dp[0]: return "Alice"
        elif dp[0] == sum - dp[0]: return "Tie"
        return "Bob"
def main():
    solution = Solution()  
    piles = [1,2,3,7]
    out = solution.stoneGameIII(piles)
    print(out) 

if __name__ == "__main__":
    main()
