from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32): # 枚举部分（位置）
            mask = 1 << i
            ones = 0 #  有多少个数在这一位是一
            for num in nums:
                if mask & num: ones += 1 # 一个数，有一个位是1，就是true. 这里，如果能 true, 必然是 mask 的位被满足了
            ans += (len(nums) - ones) * ones # 等价于 ones * (len(nums) - ones), 顺序不重要
        return ans
print(Solution().totalHammingDistance([4,14,4]))




