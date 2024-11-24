# pq: init O(n), add O(logn), pq[0]: O(1), k top O(klogn), remove O(logn), arbituary O(n)
# sortedContainer: init O(nlogn), add O(logn), a[0]: O(1), k top O(k), remove O(logn), arbitrary O(logn)
 
from bisect import bisect_left, bisect_right
from typing import List
class Solution:
    def shortestDistanceAfterQueries_BS(self, n: int, queries: List[List[int]]) -> List[int]:
        # 构建, 在前面基础上多多少，只减不增，具有唯一性; 贪心, 从必然入手 把当前的逐步, 用最优法，变成必然
        # the edge will not cross each other, which means there will be only one possible route from 0 to n - 1.
        a = list(range(1, n)); ans = []

        # a = [1, 2, 3, 4, 5], 代表 1 -> 2, 2 -> 3, ..., 5 -> END
        # 建 2 -> END
        # 我们就跳 3, 4, 5; 3 = 第一大于 2, 5 = 第一小于 END
        for l, r in queries:
            L = bisect_right(a, l)
            R = bisect_left(a, r) - 1
            for _ in range(L, R + 1): a.pop(L) # Σ O(n)
            ans.append(len(a))
            # [1, 2, 3, 4, 5] -> [1, 2, 4, 5] -> [1, 2, 5] -> [1, 2]
        return ans
    
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # 链表
        ans = []
        R = list(range(1, n)) # 节点 i 右边指向 R[i]
        print(R)
        cnt = n - 1
        for i, r in queries:
            while R[i] < r: # xxxxxx(v) R[i] = r
                cnt -= 1
                R[i], i = r, R[i]
            ans.append(cnt)
        return ans
print(Solution().shortestDistanceAfterQueries(4, [[0,3],[0,2]]))