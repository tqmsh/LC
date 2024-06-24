from typing import List 
from collections import defaultdict
from math import isqrt
class Solution: 
    def winnerSquareGame(self, n: int) -> bool:
        dp = defaultdict(int)
        # squares 模版
        squares = lambda x: (i * i for i in range(isqrt(x), 0, -1))
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - s] for s in squares(i)) # ¬(∀x ∈ D P(x)) ⟺ ∃ x ∈ D ¬P(x)
        return dp[n]
def main():
    solution = Solution()  
    n = 4
    out = solution.winnerSquareGame(n)
    print(out) 

if __name__ == "__main__":
    main()
