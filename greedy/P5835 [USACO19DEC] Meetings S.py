from bisect import bisect_left
from typing import List

def _check_get_L(vis, x, t, mid):
    # 过了 t 单位时间后，mid & 目前枚举的向左的牛相对速度为 -2, 所以位移时 -2t
    if x - 2 * t <= vis[mid]: return 1 # 够得着
    return 0

def _get_L(vis, x, t):
    l = 0; r = len(vis) - 1; ans = -1
    while l <= r:
        mid = (l + r) // 2
        if _check_get_L(vis, x, t, mid):
            ans = mid
            r = mid - 1
        else: l = mid + 1
    return ans

def check(arr, mid, L, sum_tot):   
    # 思维: 我们要分析，里面有什么样的规律; 其实在牛碰撞的时候，可以看成每头牛依旧按照原来的方向行进，只不过碰撞之后两头牛的体重等要素交换。
    # 所以，假设一只牛能走到最后，它体重等要素必然是最左/右端的牛的, 先后顺序不重要，因为最后一只牛的体重等要素谁拿不重要，能带出去最重要
    
    # 双指针
    l = 0; r = len(arr) - 1; sum_left = 0
    for _, x, d in arr:
        if d == 1 and x + mid >= L: sum_left += arr[r][0]; r -= 1
        if d == -1 and x - mid <= 0: sum_left += arr[l][0]; l += 1
    return sum_left * 2 >= sum_tot 

def count_meetings(arr: List[List[int]], L: int) -> int: 
    # 二分，最小化最大值; xxxxxx(v)vvvv, 时间越大，越有可能达成目标重量
    arr.sort(key = lambda x: x[1]); sum_tot = sum([w for w, _, _ in arr])
    # lambda 就是正对一个需要考虑的树枝，如何处理
    
    l = 0; r = 1000000000 + 10
    t = l + bisect_left(range(l, r + 1), 1, key=lambda mid: check(arr, mid, L, sum_tot))

    # 对数，等于从左往右枚举向左的牛，最远能碰到多少往右的牛，二分最大化最小值，xxxxx(v)vvvvvv COW
    ans = 0; vis = [] # vis: 一直向后看，看到的往右走的牛
    for _, x, d in arr:
        if d == -1:
            L = _get_L(vis, x, t)
            ans += len(vis) - L # [L, len(vis)) 
        else: vis.append(x) 
    return ans


print(count_meetings([[10, 1, 1], [9, 2, 1], [15, 3, -1], [12, 4, -1], [8, 5, 1], [7, 6, -1]], 20))  # 应该输出相遇的总次数
