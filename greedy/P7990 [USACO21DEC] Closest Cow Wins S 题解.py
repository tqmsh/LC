from collections import deque
from typing import List
from heapq import heappush, heappop
 
class Grassland:
    def __init__(self, pos: int, taste: int):
        self.pos = pos  
        self.taste = taste 
    def __lt__(self, other: 'Grassland'): return self.pos < other.pos
 
def max_taste(grasslands: List[Grassland], cow_positions: List[int], n: int) -> int:
    grasslands.sort()
    cow_positions = [float('-inf')] + cow_positions + [float('inf')]
    
    # 贪心，排序, 一步一步走，每一步都得最优
    picks = []

    # 双指针，指着当前需要考虑的草坪 
    j = 0 

    for i in range(1, len(cow_positions)): # 枚举一对敌对牛
        interval_sum = 0
        # 枚举区间，打擂台，求最优1
        window: deque[Grassland] = deque(); window_sum = 0; window_mx = 0; mx_window_l = (cow_positions[i] - cow_positions[i - 1]) / 2

        # j + 1 < len, 如果是 xxxxxx(v), while 跳 x
        # j < len, 如果是 (vvvvvvv)x, while 跳 v + 判断
        while j < len(grasslands) and grasslands[j].pos < cow_positions[i]: # 枚举 (l, r) 里的草坪，可以被我们吃的
            # 进 j
            window.append(grasslands[j])    
            window_sum += window[-1].taste
            interval_sum += window[-1].taste 
            # 确认 window 合法

            #              紫色                       红色            无法覆盖
            while window[-1].pos - window[0].pos >= mx_window_l: window_sum -= window[0].taste; window.popleft()
            window_mx = max(window_mx, window_sum) 
            j += 1
         
        heappush(picks, (-window_mx, interval_sum - window_mx))
                        # 第一只牛赚的    第二只牛赚的
    ans = 0
    for _ in range(n):
        if picks: 
            mx, remain = heappop(picks); mx = abs(mx)
            ans += mx
            heappush(picks, (-remain,  0))
    return ans
grasslands_input = [
    Grassland(0, 4),
    Grassland(4, 6),
    Grassland(8, 10),
    Grassland(10, 8),
    Grassland(12, 12),
    Grassland(13, 14)
]
# 5头奶牛的位置
cow_positions_input = [2, 3, 5, 7, 11]

# N = 2，最大放置2头奶牛
n_input = 2

# 执行测试
result = max_taste(grasslands_input, cow_positions_input, n_input)
print(result)  # 应输出 36