from math import floor
from bisect import bisect_left
def check(mid, arr):
    tmp = arr[:]
    run = 1
    while run:
        run = 0
        # 贪心，从必然入手，如果 < mid, 不动它，因为 i (-2), i + 1 (+1) 只会把它变得更小
        #                如果 > mid, 把多出来的全送给 i + 1, 由于 i - 2k = mid, 2|i - mid
        #                如 2∤i - mid，只有一种可能，就是让 i - 1 做操作 i - 1 (-2) i (+1)

        for i in range(len(tmp)):
            if tmp[i] <= mid: continue
            run = 1 # 需要继续修改
            if (tmp[i] - mid) % 2 != 0: tmp[(i - 1) % len(tmp)] -= 2; tmp[i] += 1
            k = (tmp[i] - mid) / 2; tmp[i] -= 2 * k; tmp[(i + 1) % len(tmp)] += k
    return all(x == mid for x in tmp)
     
def solve(arr): 
    tot = sum(arr)
    l = 0; r = floor(tot / len(arr)) 
    # BisectLeft 返回的是 Index 值，如果 Index = Val 的话 ok 的, i.e. range(), 
    # 如果不是的话，I = list(range(..)), mx = I[idx], idx = bisect left
    mx = bisect_left(range(l, r + 1), 1, key=lambda x: not check(x, arr)) - 1 
    if mx == -1: return -1 
    return tot - mx * len(arr)   


# 测试用例
if __name__ == "__main__":
    arr4 = [10, 20, 30, 40]
    print(solve(arr4))  # 输出: 30
