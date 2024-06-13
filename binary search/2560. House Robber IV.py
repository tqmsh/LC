from typing import List 
from collections import defaultdict
class Solution:
    def _is_possible(self, nums, k, capacity): #immut: int/float/str/tuple/bool; mut: list/dict/set/bytearray
        i = 0
        while i < len(nums):
            if nums[i] <= capacity:
                k -= 1
                if k == 0: return 1 # 🟥 不用走到底，枚举能用则用，一到就停
                i += 1
            i += 1
        return 0
    # 最小化最大值，二分答案
    def _get_min_capacity(self, nums, k, min_capacity_candidates):
        left = 0; right = len(min_capacity_candidates) - 1; min_capacity_index = 0
        while left <= right:
            mid = (left + right) // 2
            if self._is_possible(nums, k, min_capacity_candidates[mid]):
                min_capacity_index = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_capacity_index
    
    def minCapability(self, nums: List[int], k: int) -> int:
        min_capacity_candidates = list(sorted(set(nums)))
        return min_capacity_candidates[self._get_min_capacity(nums, k, min_capacity_candidates)] 
    
def main():
    solution = Solution()  
    nums = [2,7,9,3,1]
    k = 2
    out = solution.minCapability(nums, k)
    print(out) 

if __name__ == "__main__":
    main()
