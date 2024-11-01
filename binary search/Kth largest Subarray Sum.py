from typing import List 
from bisect import bisect_left
class Solution:
    def _check(self, mid): 
        rank = 0; sum = 0 # rank = i: i 个子数组; # sum = x: Σ [i, j] = x  
        j = 0
        for i in range(1, len(self.nums)):
            while j + 1 < len(self.nums) and sum + self.nums[j + 1] <= mid:  # vvvvv(v)x, Σ [i, j] <= mid
                sum += self.nums[j + 1]; j += 1
            rank += j - i + 1
            sum -= self.nums[i]
        return rank >= self.k
    def kthLargestSuarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums); k = (n + 1) * n // 2 - k + 1 
        nums = [0] + nums
        self.nums = nums; self.k = k
        l = min(nums); r = sum(nums)
        # 第一 mid self._check(mid) = 1
        return l + bisect_left(range(l, r + 1), 1, key = self._check) # O(nlogn)
                    
def main():
    solution = Solution()  
    matrix = [2,3,1,4]
    k = 6
    out = solution.kthLargestSuarraySum(matrix, k)
    print(out) 

if __name__ == "__main__":
    main()
