from typing import List
class Solution:
    def _greedy(self, a):
        ans = [1] * len(a) 
        for i in range(1, len(a)):
            if a[i] > a[i - 1]: ans[i] = ans[i - 1] + 1 
        return ans
    def candy(self, ratings: List[int]) -> int:
        return sum([max(x, y) for x, y in zip(self._greedy(ratings), self._greedy(ratings[::-1])[::-1])])
print(Solution().candy([1, 1, 1]))