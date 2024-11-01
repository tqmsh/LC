from functools import cmp_to_key
from typing import List
# (a b) (c d)
# wlog a <= b, c <= d, a <= c, 即 调换 ()() 顺序变不了
# 小数据
# 分类讨论：
# - 形如 (1, 2), (3, 4) 或 (1, 3), (2, 4) 或 (1, 2), (1, 3)。此时显然 (a1,1, a1,2) 在前更优。
# - 形如 (1, 4), (2, 3) 或 (1, 2), (1, 2)。此时无论谁在前都可以。
# - 形如 (1, 3), (1, 2)，此时 (a2,1, a2,2) 在前更优。
# 可以发现当 a1,1 < a2,1 时 (a1,1, a1,2) 在前一定不劣。当 a1,1 = a2,1 时，若 a1,2 ≤ a2,2 则 (a1,1, a1,2) 在前不劣，否则 (a2,1, a2,2) 在前不劣。


def cmp(a: List[int], b: List[int]):
    def f(x): return -1 if x else 1
    if min(a) != min(b): return f(min(a) < min(b))
    return f(max(a) < max(b))

# 邻项交换法, 为了跟小，让min小的放前面，如果一样，让max小的放前面，这样被杀可能性小 - 向右俯视 = 杀；把 min 放越左越好 - 被杀可能性小，把 max 放越左越好 - 杀别人可能性小
# 或者用和来比较
def solve(a: List[List[int]]):
    return sorted(a, key = cmp_to_key(cmp))

pairs = [[2, 3], [5, 10], [9, 6], [4, 1], [8, 7]]
result = solve(pairs)
print(result)  # Outputs the pairs in optimal order
