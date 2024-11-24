from typing import List

class Node:
    def __init__(self, a, b): self.a = a; self.b = b
    def __lt__(self, other: 'Node'): return self.a < other.a 

def isok(arr: List[Node], mid, k, idx):
    # 贪心：(位置，时间)能晚一点，则晚一点; 用最少的贡献，做想要的中位数
    cnt = 0 # >= mid 的数字
    for i in range(len(arr) - 1, -1, -1):
        if arr[i].a >= mid: cnt += 1; continue

        if arr[i].b:
            if k >= mid - arr[i].a: k -= (mid - arr[i].a); cnt += 1; continue
            break # i 满足不了，更小的 i-1 必然不行
    
    req = len(arr) - idx # [idx, -1) 必然 >= mid
    return cnt >= req

def _get_med_max(arr: List[Node], idx, k): # O(log (1e9))
    # 最大化最小值，二分枚举中位数 vvvvvvvv(v)x
    l = arr[idx].a; r = arr[idx].a + k; ans = 0
    while l <= r:
        mid = (l + r) // 2
        if isok(arr, mid, k, idx):
            ans = mid
            l = mid + 1
        else: r = mid - 1
    return ans

def _get_med_static(i, idx, arr: List[Node]):
    if i <= idx: return arr[idx + 1].a # 把它移走了，整体左移影响到中位数位置了
    return arr[idx].a

def max_score(a: List[int], b: List[int], k: int) -> int:
    arr: List[Node] = [Node(a[i], b[i]) for i in range(len(a))]
    arr.sort()

    # 我们有k次增值的机会，是加到ai（不会改变中位数）上 还是 增值后改变中位数（此时中位数可能改变）？ 
    
    # 贪心：一步一步走，每一步都得最优
    idx = (len(a) - 1) // 2; ans = 0
    for i, node in enumerate(arr):
        # fix i
        # 想最大化 max(a[i] + 中位数), 如果 b[i] == 1, 每一次 k 增值，最优就是加在 a[i] 上，因为一定可以让其变大，但不一定可以让中位数变大
        if node.b: ans = max(ans, (node.a + k) + _get_med_static(i, idx, arr))

    # 如果 b[i] == 0, 只能二分中位数，在这个情况下，贪心取最大的 a[i]， 即 a[-1], 所以其实这个情况只用考虑一次，因为其他时候考虑必然打擂台打不过取 a[-1]
    if not arr[-1].b: ans = max(ans, arr[-1].a + _get_med_max(arr, idx, k))
    return ans

print(max_score([7,5,2,5,4], [0,0,1,0,1], 4))  # 输出应为 16
print(max_score([3, 3, 3], [0, 0, 0], 10))  # 输出应为 6
print(max_score([2, 1, 5, 1], [0, 1, 0, 1], 4))