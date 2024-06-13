from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        # 枚举，能用则用
        # you dont have to worry about selling at a low point, because
        min = float('inf')
        profit = 0
        for price in prices:
            if price < min:
                min = price
            else:
                profit += price - min
                min = price
        return profit
def main():
    solution = Solution()  
    prices = [7,1,5,3,6,4]
    out = solution.maxProfit(prices)
    print(out) 

if __name__ == "__main__":
    main()
