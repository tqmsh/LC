from typing import List
def min_board_length(m: int, stalls: List[int]) -> int:
    # Case 1: 足够 
    if m >= len(stalls): return len(stalls)
    # Case 2: 不够，得拆
    stalls.sort()
    # [stalls[0], stalls[-1]]
    ans = stalls[-1] - stalls[0] + 1
    # 正难则反，假装一个长条，有一会断开 m - 1 块

    # (..., stalls[i - 1]] (stalls[i - 1], stalls[i]) = gap [stalls [i], ...)
    gaps = [stalls[i] - stalls[i - 1] - 1 for i in range(1, len(stalls))]
    # 贪心，
    gaps.sort(reverse = 1)
    for i in range(m - 1): ans -= gaps[i]
    return ans

