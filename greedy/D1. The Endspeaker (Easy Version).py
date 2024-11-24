from typing import List
from itertools import accumulate

def minimum_cost_to_empty_aay(a: List[int], b: List[int]) -> int:
    m = len(b); a = [0] + a; b = [0] + b  # 保证数组从索引 1 开始
    # 无解
    if max(a) > b[1]: return -1  # 修正条件：应为 `max(a) > b[1]`
    psa = list(accumulate(a))  # 计算前缀和
    dp = [float('inf')] * len(a)  # 初始化 dp 数组为无穷大
    dp[0] = 0  # 初始条件

    # 遍历每个 k（即 b 的索引，从 1 开始）
    for k in range(1, len(b)):
        L = 0  # 双指针做 Σ(L, R] <= b[k]，区间枚举优化
        for R in range(1, len(a)):
            # 贪心：(位置，时间)能左一点，则左一点; 用最少的贡献，做 dp[L], 因为 (m - k) 都一样
            while L + 1 < len(a) and psa[R] - psa[L] > b[k]: L += 1  # xxxxxx(v)vvvvv -> 最小化最大值
            dp[R] = min(dp[R], dp[L] + (m - k))  # 更新 dp[R]

    return dp[-1] 
print(minimum_cost_to_empty_aay([9, 3, 4, 3], [11, 7]))  # 应输出 1
print(minimum_cost_to_empty_aay([20], [19, 18]))  # 应输出 -1
print(minimum_cost_to_empty_aay([2, 5, 2, 1, 10, 3, 2, 9, 9, 6], [17, 9]))  # 应输出 2