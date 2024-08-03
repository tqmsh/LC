from typing import List

def solve(a: List[int], b: List[int]) -> int:
    n = len(a)
    a = [0] + a
    b = [0] + b
    dp = [[0] * 3 for _ in range(n + 1)]

    dp[1][0] = a[1]
    dp[1][1] = b[1]
    dp[1][2] = float('inf') 

    for i in range(2, n + 1): 
        dp[i][0] = a[i] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][1] = b[i] + min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) # b 联通快 不以 i 结尾
        dp[i][2] = b[i] + b[i - 1] + min(dp[i - 2][0], dp[i - 2][1], dp[i - 2][2]) # b 联通快 以 i 结尾 
    result = min(dp[n][0], dp[n][2]) 
    return result

# Test the function with the given example
a = [7, 3, 9, 1, 6, 5, 8, 4, 2, 10]
b = [4, 8, 2, 7, 5, 6, 3, 9, 1, 7]

print(solve(a, b))
