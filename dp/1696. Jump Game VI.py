from typing import List 
from collections import defaultdict, deque
import math
class Solution: 
    # 单调队列，模版
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque([0])
        dp = defaultdict(int); dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            while dq and dq[0] < i - k: dq.popleft() # 维持 [i - k, i)；跳 (-∞, i - k) 的
            dp[i] = dp[dq[0]] + nums[i]
            
            while dq and dp[i] >= dp[dq[-1]]: dq.pop()  # 维持 [i - k, i] 最大值; 跳 <= 
                                                        # dp[i] 的，维持一个单调递减的 dq, 左边就是最大的
            dq.append(i)
        
        return dp[len(nums) - 1]
        
def main():
    solution = Solution()  
    nums = [1,-1,-2,4,-7,3]; k = 2
    out = solution.maxResult(nums, k)
    print(out) 

if __name__ == "__main__":
    main()
