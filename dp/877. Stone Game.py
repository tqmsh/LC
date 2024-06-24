from typing import List 
from collections import defaultdict  
class Solution:
    def stoneGame(self, piles):
        dp = defaultdict(int) 

        for i in range(len(piles)): dp[i, i] = piles[i]    
        for l in range(2, len(piles) + 1): 
            for i in range(len(piles)):  
                j = i + l - 1  
                if j >= len(piles): break 
                dp[i, j] = max(piles[j] - dp[i, j - 1], piles[i] - dp[i + 1, j]) 
 
        return dp[0, len(piles) - 1] > 0 

# Example usage:
solution = Solution()
print(solution.stoneGame([5, 3, 4, 5]))  # Output should be True

def main():
    solution = Solution()  
    piles = [5,3,4,5]
    out = solution.stoneGame(piles)


if __name__ == "__main__":
    main()
