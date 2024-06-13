from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        ans = 0
        for i in range(2, len(prices)): 
            mn = min(mn, prices[i])
            print(mn, prices[i])
            ans = max(ans, prices[i] - mn)
        return ans
                    
def main():
    solution = Solution()  
    prices = [7,1,5,3,6,4]
    out = solution.maxProfit(prices)
    print(out) 

if __name__ == "__main__":
    main()
