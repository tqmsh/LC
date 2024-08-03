from typing import List 
from collections import defaultdict
from itertools import accumulate
class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:  

        n = len(nums) 
        psa = [0] + list(accumulate(nums))
        nums = [0] + nums
        dp = [[0] * (3 + 1) for _ in range(n + 1)]
         
        for i in range(k, n + 1):
            for j in range(1, 3 + 1):  
                dp[i][j] = max(dp[i - 1][j], dp[i - k][j - 1] + psa[i] - psa[i - k])
         
        i = n; j = 3; ans = []
        while i >= k and j > 0: # 字典序最小
            if dp[i - 1][j] == dp[i][j]: i -= 1 # 能不选，则不选
            else:
                ans.append(i - k)
                i -= k
                j -= 1
        return ans[::-1]


        
def main():
    solution = Solution()  
    nums = [1,2,1,2,1,2,1,2,1]; k = 2
    print(solution.maxSumOfThreeSubarrays(nums, k))   

if __name__ == "__main__":
    main()
