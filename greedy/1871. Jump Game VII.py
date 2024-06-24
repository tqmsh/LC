from collections import defaultdict
class Solution:  
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = defaultdict(int)
        # dp[i]: 至 i, 多少位置能够到达
        # dp[i] = dp[i - 1] + 1, if s[i] = 0 & i 可到达, i.e. dp[i - mn] - dp[i - mx - 1] > 0, 即存在一个点可以到这里, i >= mn
        # dp[i] = 1, i < mn

        for i in range(0, minJump): dp[i] = 1
        # print(dp[0], dp[1])
        for i in range(minJump, len(s)):
            # print(dp[0], dp[1])
            # print(i, i - minJump, dp[max(0, i - minJump)], i - maxJump - 1, dp[max(-1, i - maxJump - 1)]) 
            if s[i] == '0' and dp[max(0, i - minJump)] - dp[max(-1, i - maxJump - 1)] > 0:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
        return dp[len(s) - 1] - dp[len(s) - 1 - 1] == 1

def main():
    solution = Solution()  
    s = "01101110"; minJump = 2; maxJump = 3
    out = solution.canReach(s, minJump, maxJump)
    print(out) 

if __name__ == "__main__":
    main()
