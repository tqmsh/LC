from typing import List 
class Solution:
    def smallestRangeII(self, a: List[int], k: int) -> bool: 
        a = sorted(a)
        ans = a[len(a) - 1] - a[0] 
        for i in range(len(a) - 1): # 枚举分割情况, [0, i] + k, (i, n] - k
            ans = min(ans, max(a[i] + k, a[len(a) - 1] - k) - min(a[0] + k, a[i + 1] - k)) # i + 1 < len(a), i < len(a) - 1
        return ans

print(Solution().smallestRangeII([0, 10], 2))