from typing import List 
class Solution:
    def _rob_linear(self, nums):
        dp = [0] * len(nums)
        if len(nums) == 1: return nums[0]
        dp[0] = nums[0]; dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        # 可能的情况枚举
        # 必然是 [0, n) 或者是 (0, n] 选最大 
        if len(nums) == 1: return nums[0]
        return max(self._rob_linear(nums[:-1]), self._rob_linear(nums[1:]))
    
def main():
    solution = Solution()  
    nums = [2,3,2]
    out = solution.rob(nums)
    print(out) 

if __name__ == "__main__":
    main()
