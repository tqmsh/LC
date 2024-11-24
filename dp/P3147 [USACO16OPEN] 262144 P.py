def max_number(arr): 
    n = len(arr); arr = [0] + arr
    dp = [[0] * (58 + 1) for _ in range(n + 1 + 1)]# log(262144) + 40 = 58, 就是最大能做出来的数字
            # 第一个 + 1 因为 可能会问到 n + 1, 第二个 + 1 因为R 会开到  0index -> 1index
 
    # dp[i][x]: 以 i 为左端点，合并出数字 x 的右端点, [i, dp[i][x]) 能合并出 x
    # dp[i][x] = dp[dp[i][x - 1]][x - 1]
    # dp[i][arr[i]] = i, i ∈ [1, n]
    for i in range(1, n + 1): dp[i][arr[i]] = i 
    ans = 0
    for x in range(2, 58 + 1): # 贪心；滚雪球思想，从小往上滚, 枚举能用则用，能变多少大的就变多少大的
        for i in range(1, n + 1):  
            # arr[i] != x,      存在跳板
            if not dp[i][x] and dp[i][x - 1] and dp[dp[i][x - 1] + 1][x - 1]: dp[i][x] = dp[dp[i][x - 1] + 1][x - 1] 
            if dp[i][x]: ans = x # 答案枚举: vvv(v)x
    return ans 
