def solve(arr): 
    from collections import Counter
    import math
    # 贪心：从小到大排序，枚举极数能用则用
     
    freq = Counter(arr) 
    pair_count = sum(count // 2 for count in freq.values())
 
    if pair_count < 4: return "NO"
        
    mx1 = -math.inf  # 第一大的值
    mx2 = -math.inf  # 第二大的值
    mn1 = math.inf   # 第一小的值
    mn2 = math.inf   # 第二小的值


    for val, count in freq.items():
        if count >= 4:
            # 如果某个值至少出现 4 次，则可以同时充当最大值和最小值
            mx1 = max(mx1, val)
            mx2 = max(mx2, val)
            mn1 = min(mn1, val)
            mn2 = min(mn2, val)
        elif count >= 2:
            # 最大 次大 模版 
            # 如果某个值至少出现 2 次，可以作为潜在的次大值或次小值
            if val > mx1:
                mx2 = mx1
                mx1 = val
            elif val > mx2:
                mx2 = val

            if val < mn1:
                mn2 = mn1
                mn1 = val
            elif val < mn2:
                mn2 = val

    # 输出结果，按构造的 8 个点顺序排列
    return f"YES\n{mn1} {mn2} {mn1} {mx1} {mx2} {mn2} {mx2} {mx1}"


# 测试用例
if __name__ == "__main__":
    # 测试用例 1
    arr1 = [-5, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 10]
    print(solve(arr1))  # 输出: YES 和 8 个点

    # 测试用例 2
    arr2 = [0, 0, -1, 2, 2, 1, 1, 3]
    print(solve(arr2))  # 输出: NO

    # 测试用例 3
    arr3 = [0, 0, 0, 0, 0, 5, 0, 5]
    print(solve(arr3))  # 输出: YES 和 8 个点
