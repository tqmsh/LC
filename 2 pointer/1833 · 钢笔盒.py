class Solution:
    def minimumBoxes(self, boxes, target):
        n = len(boxes); boxes = [0] + boxes + [0]; 
        dp = [0] * (n + 1); dp[0] = float('inf') # dp[i]表示区间[0, i]最短的合法区间长度
        j = 0; path = 0
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            # path: [j, i)
            path += boxes[i]
            while path > target:
                path -= boxes[j]
                j += 1
            while j < i and boxes[j] == 0: j += 1 # 能不选则不选
            # path: [j, i]
            if path == target: dp[i] = min(dp[i], i - j + 1)
        j = n + 1; path = 0; ans = float('inf')
        for i in range(n, 0, -1):
            # path: (i, j]
            path += boxes[i]
            while path > target: 
                path -= boxes[j]
                j -= 1
            while j > i and boxes[j] == 0: j -= 1
            # path: [i, j]
            if path == target and j + 1 <= n: ans = min(ans, j - i + 1 + dp[j + 1])
        return 0 if ans == float('inf') else ans

boxes = [1, 1, 1, 1, 1, 1, 1]
target = 3
output = Solution().minimumBoxes(boxes, target)
print("输出:", output)  # Expected output: 4
