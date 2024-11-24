from typing import List
from heapq import heapify, heappop, heappush

def min_effort_fruit_merge(fruits: List[int]) -> int:
    heapify(fruits) # O(n)
    ans = 0
    for _ in range(len(fruits) - 1):
        a = heappop(fruits)
        b = heappop(fruits)
        ans += a + b
        heappush(fruits, a + b)
    return ans

print(min_effort_fruit_merge([1, 2, 9]))  # 预期输出：15