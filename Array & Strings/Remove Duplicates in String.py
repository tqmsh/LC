from typing import List
from collections import Counter

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:  
        # cnt = 1
        # for i in range(1, len(s)):
        #     if s[i] == s[i - 1]: cnt += 1
        #     else: cnt = 1
        #     if cnt == k: return self.removeDuplicates(s[:i - k + 1] + s[i + 1:], k) 
        # return s # 基，即不存在任何重复的，即返回自身
 
        # stk 模版
        stk = [['.', 0]]; 
        for c in s:
            if stk[-1][0] == c: 
                stk[-1][1] += 1
                if stk[-1][1] == k: stk.pop() # 消除
            else: stk.append([c, 1])
        
        # ch * 模版
        return ''.join(c * f for c, f in stk) 
def main():
    solution = Solution() 
    s = "deeedbbcccbdaa"; k = 3
    out = solution.removeDuplicates(s, k)
    print(out) 

if __name__ == "__main__":
    main()