
from typing import List 
from collections import deque

class Solution: 
    def _dfs(self, current_idx, current_sum, nums, target):
        if current_idx < 0: return current_sum == target  
        return self._dfs(current_idx - 1, current_sum + nums[current_idx], nums, target) +  self._dfs(current_idx - 1, current_sum - nums[current_idx], nums, target) 
 
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # 从后至前状态转移，dfs(i, j): [i, n], 满足合为 j, 有多少办法
                    #    dfs(i, j) = dfs(i - 1, j - a[i]) + dfs(i - 1, j + a[i])
                    #    combination sum 同款递归处理方式
        return self._dfs(len(nums) - 1, 0, nums, target)  
    
def main(): 
    solution = Solution() 
    nums = [7,46,36,49,5,34,25,39,41,38,49,47,17,11,1,41,7,16,23,13]; target = 3
    out = solution.findTargetSumWays(nums, target) 
    print(out) 

if __name__ == "__main__":
    main()