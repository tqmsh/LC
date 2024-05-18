from typing import List
from collections import Counter

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # 位运算 模版
        mx = (0, 0) 
        s_b = bytearray(s.encode())
        

        for i in range(len(s)):
            l, u = 0, 0
            for j in range(i, len(s)): # 区间枚举 
                # 小写 大写 模版
                if (s_b[j] >= ord('a')): # 小写 
                    l |= 1 << (s_b[j] - ord('a')) # 录 x
                else:
                    u |= 1 << (s_b[j] - ord('A'))  
                if l == u and j - i + 1 > mx[1] - mx[0]: #!🟥mx维持[i, j + 1]防止'c'这样的 Edge case, 因为如果是 [i, j] 的话，初始化 (0, 0) 就是集合为 0，而非空 !
                    mx = (i, j + 1)   
        return s[mx[0]: mx[1]]
 
    def tb(self, l: int):
        return bin(l)[2:].zfill(26)

        
# s_b[mx[0]:mx[1] + 1].decode()

    
def main():
    solution = Solution()
    
    s = "c"
    out = solution.longestNiceSubstring(s)
    print(out) 

if __name__ == "__main__":
    main()