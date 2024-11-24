from typing import List
from bisect import bisect_left

def check(mid, arr):
    # 贪心：排序按照位置，让你舍生处地，哪一种方法最划算; 滚雪球思想，从小到大滚，先用最友善的牛把这个牛往上顶，把有效顶区间变大，这样那些不友善的牛就更可能可以顶你
    
    L = mid # 一开始插队插至 [mid, len) 都可以把 mid 顶到前面
    for c in sorted(arr[:mid]): # (idx, len) = 被插队的 c 牛, c = len - idx - 1, idx = len - 1 - c
        idx = len(arr) - 1 - c
        if idx >= L: L -= 1 # 这只友善的牛成功把我们往上顶了，有效顶区间增加
        else: return 0 # 最友善的都顶不了，剩下的不用考虑了
    return 1

def greedy_gift_takers(arr: List[int]) -> int:
    # 牛是否能拿到礼物 vvvvvv(x)xx, 如果一头牛拿不到礼物，那么他后面的牛也都拿不到礼物，如果一头牛拿的到礼物，那么他前面的牛也都拿的到礼物
    
    # 答案: [第一 x, len), 二分 第一 x, len - 第一 x 
    l = 0; r = len(arr) - 1 

    
    mn_idx = l + bisect_left(range(l, r + 1), 1, key = lambda x: not check(x, arr))  
    # print(check(2, arr)) 
    return len(arr) - mn_idx
print(greedy_gift_takers([2, 43, 5, 1, 2, 4, 5, 2]))