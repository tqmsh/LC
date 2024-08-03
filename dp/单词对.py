from typing import List 
def dd_bit(num): return bin(num)[2:]  
    
class Solution:
    # 状压 模版
    def _mask(self, word):
        ans = 0
        for c in word:
            ans |= 1 << (ord(c) - ord('a'))  
        return ans
    def max_product(self, words):
        # 初始化
        dp = [0] * (1 << 3) # debug, 26
        b = {}
        for word in words: 
            b[word] = self._mask(word)
            dp[b[word]] = len(word) 
        # 状态转移
        for i in range(2 ** 3): #debug, 26
            for idx in range(3):
                if i & (1 << idx):
                    j = i & ~(1 << idx) 
                    dp[i] = max(dp[i], dp[j])
        ans = 0
        for word in words: ans = max(ans, len(word) * dp[~b[word] & ((1 << 3) - 1)])  
        return ans

# Example usage
solution = Solution()
words = ["ab", "ab", "c"]
print(solution.max_product(words))  # This will print the result