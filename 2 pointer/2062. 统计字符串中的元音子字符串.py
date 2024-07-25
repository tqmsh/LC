from typing import List 
from collections import defaultdict 
class Solution:
    def countVowelSubstrings(self, s: str) -> int:
        # 重启双指针 + 包含/不包含 + 不求最短/求所有
        
        l_r = l_l = 0 # start是一段连续元音的左端点，只有遇到辅音时才变化，l是最短有效子串的左端点，只要cnt[l] > 1就会右移
        cnt = defaultdict(int); v = "aeiou"; ans = 0
        
        for r, c in enumerate(s): # 枚举 R 
            if c in v:
                cnt[c] += 1 # 把枚举的 R 的内容给进去

                while cnt[s[l_r]] > 1: # l_r 指针 随着 r 的右移，而增加，所以双指针
                    cnt[s[l_r]] -= 1
                    l_r += 1
                
                if len(cnt) == 5: ans += l_r - l_l + 1  # 以 i 为右端点的子串，左端点范围 [l_l, l]
        
            else:
                cnt.clear()
                l_l = r + 1
                l_r = r + 1

        return ans
                
def main():
    solution = Solution()  
    s = "cuaieuouac"
    out = solution.countVowelSubstrings(s)
    print(out) 

if __name__ == "__main__":
    main()
