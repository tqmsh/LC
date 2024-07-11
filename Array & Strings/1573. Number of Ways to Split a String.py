from typing import List
from collections import Counter

class Solution:
    def numWays(self, s: str) -> int: 
        ones_idx = []; MOD = 10 ** 9 + 7
        for i, ch in enumerate(s): 
            if ch == '1': ones_idx.append(i) 
        # 离散化，枚举有效位置
        tot = len(ones_idx); req = tot//3
        if tot == 0: return (len(s) - 1) * (len(s) - 2) // 2 % MOD
        if tot % 3 != 0: return 0 
                # 第一个竖杠的选择
        return (ones_idx[req] - ones_idx[req - 1]) * (ones_idx[2 * req] - ones_idx[2 * req - 1]) % MOD

        
# s_b[mx[0]:mx[1] + 1].decode()

    
def main():
    solution = Solution()
    
    s = "10101" 
    out = solution.numWays(s)
    print(out) 

if __name__ == "__main__":
    main()