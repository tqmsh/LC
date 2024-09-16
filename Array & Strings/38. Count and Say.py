from typing import List
from collections import Counter

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        s = list(self.countAndSay(n - 1)) 
        ans = ""
        cnt = 1; lst = "x"

        for ch in s:
            if ch == lst: cnt += 1
            else: 
                if lst != -1: ans += f"{cnt}{lst}"
                cnt = 1

            lst = ch  
        ans += f"{cnt}{lst}"
        return ans[2:]
    
# s_b[mx[0]:mx[1] + 1].decode()

# 邮箱，登陆，付钱，DDL +, 必然登陆
    
def main():
    solution = Solution()
    
    n = 5
    out = solution.countAndSay(n)
    print(out) 

if __name__ == "__main__":
    main()