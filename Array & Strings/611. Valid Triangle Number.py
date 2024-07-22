from typing import List
from bisect import bisect_left, bisect_right

class Solution: 
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(num for num in nums if num > 0) # 🟥 Edge Case, 0 不行

        # 二分
        ans = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                # 枚举 L 算 R 
                k = bisect_left(nums, nums[i] + nums[j]) # 第一 >= sum  
                ans += k - (j + 1) # [j + 1, k) 都能用

        # 双指针
        ans = 0
        for x in range(len(nums) - 1, 1, -1): #[2, n]
            i = 0; j = x - 1
            while i < j: # i, j 两个数不能重叠
                if nums[i] + nums[j] > nums[x]:
                    # 枚举 L 算 R（# 合法区间）
                    ans += j - i # [i, j) 里都可以做 A 和 位于 j 坐标的 B 配对
                    j -= 1 # LF 变小试试
                else:
                    i += 1 # LF 变大试试
        return ans
    
def main():
    solution = Solution()
    
    nums = [7]
    out = solution.triangleNumber(nums)
    print(out) 

if __name__ == "__main__":
    main()