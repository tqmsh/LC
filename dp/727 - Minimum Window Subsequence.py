# O(n * n * m) 暴力，过不了
# O(n m) 二维 dp, 可以，事情反常就一定有奇怪的地方，比如说 m = 100, 明摆着让你二维 dp 枚举 m, ...
# O(n) 一般的， ... 你傻乎乎搞双指针，即是以前的都是这样的，但是是因为mp & cnt好维持，这次不一样，别一棵树上吊死，看看别的算法，两个字符串就二维 dp

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:  
        dp = [[-1] * len(s2) for _ in range(len(s1))] 
        for i in range(len(s1)):
            if s1[i] == s2[0]: dp[i][0] = i 

        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if s1[i] == s2[j]: dp[i][j] = dp[i - 1][j - 1] 
                else: dp[i][j] = dp[i - 1][j]  # 如果 s1 前 i - 1 可以应付，那也可以，如果不行的话，那么拉倒
            
        mn = float('inf')
        l = -1
        for i in range(len(s1)):
            if dp[i][len(s2) - 1] != -1:
                lenn = i - dp[i][len(s2) - 1] + 1
                if lenn < mn:
                    mn = lenn
                    l = dp[i][len(s2) - 1]
        return "" if mn == float('inf') else s1[l:l + mn]

def main():
    solution = Solution()  
    s1 = "abcd"; s2 = "bcd"
    out = solution.minWindow(s1, s2)
    print(out) 

if __name__ == "__main__":
    main()
