from typing import List 
from collections import defaultdict
from bisect import bisect_left 
import math
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int: 
        offers.sort(key = lambda x: x[1])         
        dp = [0] * len(offers); dp[0] = offers[0][2] 
        r_all = [offer[1] for offer in offers] 
        for i in range(1, len(offers)): 
            l, gold = offers[i][0], offers[i][2]
            j = bisect_left(r_all, l) - 1
            dp[i] = max(dp[i - 1], gold + dp[j])
        return max(dp) 
        
def main():
    solution = Solution()  
    n = 4; offers = [[1,3,10],[1,3,3],[0,0,1],[0,0,7]]
    out = solution.maximizeTheProfit(n, offers)
    print(out) 

if __name__ == "__main__":
    main()
