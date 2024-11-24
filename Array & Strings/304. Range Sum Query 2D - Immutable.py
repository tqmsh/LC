from typing import List
from itertools import accumulate
def min_differences(arr: List[int]) -> List[int]:
    arr = [0] + arr; psa = list(accumulate(arr))
    subarr = []
    
    for L in range(1, len(arr)): # O(n (n + 1) / 2)
        for R in range(L, len(arr)): subarr.append((psa[R] - psa[L - 1], L, R))
    
    # 排序
    subarr.sort()

    # 贪心，从小到大排个序，显然相邻的两个区间除去交集之后的部分就可以拿来更新，因为这两个区间变同样差距最小
    # 正难则反，逆着维护，也就是根据区间来更新所有的合法 idx, 而不是枚举 idx，然后找相邻的两个区间

    ans = [float('inf')] * len(arr)
    for i in range(1, len(subarr)):
        d1, L1, R1 = subarr[i - 1]; d2, L2, R2 = subarr[i]; d = abs(d2 - d1)
        legal = [0] * len(arr)
        for j in range(L1, R1 + 1): legal[j] ^= 1
        for j in range(L2, R2 + 1): legal[j] ^= 1
        for j in range(1, len(arr)):
            if legal[j]: ans[j] = min(ans[j], d)
    return ans[1:]

    
# 测试样例
test_case1 = [2, -3]
test_case2 = [3, -10, 4]

# 输出测试
print(min_differences(test_case1))  # 输出应为 [2, 3]
print(min_differences(test_case2))  # 输出应为 [1, 6, 1]