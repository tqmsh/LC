from collections import defaultdict
from typing import List
def max_beautiful_segments(arr: List[int]) -> int:
    psa = 0; ans = 0
    prev_idx = -1 # 上一次成为答案的最右边的坐标
    L = defaultdict(lambda: -float('inf')) # 上一次 psa 出现的位置
    L[0] = -1
    for i, x in enumerate(arr):
        psa += x
        # 区间枚举优化，枚举 R O(1) 找 L
        # 贪心, 枚举能用则用
        if L[psa] >= prev_idx: # Σ (L[psa], i] = 0
            ans += 1
            prev_idx = i
        L[psa] = i
    return ans



# Test Cases
if __name__ == "__main__":
    print(max_beautiful_segments([2, 1, -3, 2, 1]))  # Expected output: 1
    print(max_beautiful_segments([12, -4, 4, 43, -3, -5, 8]))  # Expected output: 2
    print(max_beautiful_segments([0, -4, 0, 3, 0, 1]))  # Expected output: 3
