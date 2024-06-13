from typing import List 
from collections import defaultdict
import math
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold_stock = -math.inf
        hold_money = 0 

        for price in prices: 
            hold_money = max(hold_money, hold_stock + price - fee)
            hold_stock = max(hold_stock, hold_money - price) 

        return hold_money 
def main():
    solution = Solution()  
    nums = [1,3,7,5,10,3]
    out = solution.maxProfit(nums, 3)
    print(out) 

if __name__ == "__main__":
    main()
