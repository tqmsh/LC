from itertools import accumulate
def minimum_partition_difference(points):
    n = len(points)
    points = [(0,0)] + points + [(float('inf'), float('inf'))]
    xSorted = sorted(points, key = lambda x: (x[0], x[1]))
    ySorted = sorted(points, key = lambda x: (x[1], x[0]))
    psa_xSorted_y_mx = [float('-inf')] * len(points); psa_ySorted_x_mx = [float('-inf')] * len(points)
    psa_xSorted_y_mn = [float('inf')] * len(points); psa_ySorted_x_mn = [float('inf')] * len(points)
    ssa_xSorted_y_mx = [float('-inf')] * len(points); ssa_ySorted_x_mx = [float('-inf')] * len(points)
    ssa_xSorted_y_mn = [float('inf')] * len(points); ssa_ySorted_x_mn = [float('inf')] * len(points)
    for i in range(1, n + 1):
        psa_xSorted_y_mx[i] = max(psa_xSorted_y_mx[i - 1], xSorted[i][1]); psa_ySorted_x_mx[i] = max(psa_ySorted_x_mx[i - 1], ySorted[i][0])
        psa_xSorted_y_mn[i] = min(psa_xSorted_y_mn[i - 1], xSorted[i][1]); psa_ySorted_x_mn[i] = min(psa_ySorted_x_mn[i - 1], ySorted[i][0])

    
    for i in range(n, 0, -1):   
        ssa_xSorted_y_mx[i] = max(ssa_xSorted_y_mx[i + 1], xSorted[i][1]); ssa_ySorted_x_mx[i] = max(ssa_ySorted_x_mx[i + 1], ySorted[i][0])
        ssa_xSorted_y_mn[i] = min(ssa_xSorted_y_mn[i + 1], xSorted[i][1]); ssa_ySorted_x_mn[i] = min(ssa_ySorted_x_mn[i + 1], ySorted[i][0])

    tot = (xSorted[n][0] - xSorted[1][0]) * (ySorted[n][1] - ySorted[1][1])
    ans = float('-inf')
    for i in range(1, n): # 离散化，枚举有效分割点  
        # (1) + (2)
        fir = (xSorted[i][0] - xSorted[1][0]) * (psa_xSorted_y_mx[i] - psa_xSorted_y_mn[i]) + \
              (xSorted[n][0] - xSorted[i + 1][0]) * (ssa_xSorted_y_mx[i + 1] - ssa_xSorted_y_mn[i + 1])
        # (3) + (4), 看图
        sec = (ssa_ySorted_x_mx[i + 1] - ssa_ySorted_x_mn[i + 1]) * (ySorted[n][1] - ySorted[i + 1][1]) + \
              (psa_ySorted_x_mx[i] - psa_ySorted_x_mn[i]) * (ySorted[i][1] - ySorted[1][1])
        ans = max(ans, tot - min(fir, sec))
    return ans

# 测试用例
test_points = [
    (4, 2),
    (8, 10),
    (1, 1),
    (9, 12),
    (14, 7),
    (2, 3)
]
result = minimum_partition_difference(test_points)
print(result)  # 根据题目数据计算的结果