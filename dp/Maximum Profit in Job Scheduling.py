from bisect import bisect_left
from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        a = [(0, 0, 0)] + sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        ets = [x[1] for x in a]
        dp = [0] * len(a)
        for i in range(1, len(a)):
            st, _, v = a[i]
            idx = bisect_left(ets, st + 1) - 1 # 第一个比 st + 1 小，即最晚合法
            dp[i] = max(dp[i - 1], dp[idx] + v)
        return dp[len(a) - 1]
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

print(Solution().jobScheduling())