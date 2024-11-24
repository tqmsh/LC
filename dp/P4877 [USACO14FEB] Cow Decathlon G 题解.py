from typing import List, Tuple
from functools import cmp_to_key
from collections import defaultdict
def cnt(s): return bin(s).count('1')
def max_score(val: List[List[int]], bonuses: List[Tuple[int, int, int]]) -> int: 
    n = len(val); # n: 有多少场比赛
    val_1_idx = [[0] * (len(val) + 1)] + [[0] + r for r in val] # a[i][j]: 牛 i 在比赛 j 的表现
    
    e: defaultdict[int, List[Tuple[int, int]]]= defaultdict(list) # 前 k 个活动，如果得分超过 p, 奖励 a
    for k, p, a in bonuses: e[k].append((p, a))  

    # 贪心，奖励瓶颈从小到大枚举，让你舍生处地，哪一种方法最划算, 滚雪球思想，从小到大滚，从大到小滚不了，在小的时候积累的东西可以帮助你积累大的
    for k in range(1, n): e[k].sort() # 枚举前 k 比赛
   
    dp = [0] * (1 << n)
    # dp[s]: 前 cnt(s) 场比赛，用 s 子集的牛，最优秀时能拿多少, 这里必然是前 cnt(s), 因为不这样的话，你都拿不了 e[k]
    # dp[s] =  max(dp[s], dp[s - j] + val[j][cnt(s)]), j ∈ s
    # dp[0] = 0

    # O(n n^2)
    for s in range(1, 1 << n): # 比如说 3 个牛，得做 111, 那就是 1000 - 1, 也就是 1 << 3 - 1, 就是 1 << n - 1
        for j in range(1, n + 1): # 枚举最后一场比赛是子集中的哪一头牛 j 参战 
            if (s & (1 << (j - 1))): # BitMask 是 0 Index 的
                dp[s] = max(dp[s],                                            dp[s ^ (1 << (j - 1))]                 +    val_1_idx[j][cnt(s)])
                          # 前 cnt(s) - 1 场比赛，用不包括 j 的子集参战，最优解      用 j 在第 cnt(s) 比赛中的结果
                          
        # 前 cnt(s) 场比赛完成了，准备拿奖励
        for p, a in e[cnt(s)]: 
            if dp[s] >= p: dp[s] += a 
    return dp[(1 << n) - 1] # 所有比赛选好

# 示例测试用例
val = [
    [5, 1, 7],
    [2, 2, 4],
    [4, 2, 1]
]

bonuses = [
    (2, 7, 6)  # 对前两个项目，如果分数达到7分，奖励6分
]

print(max_score(val, bonuses))  # 应输出17
