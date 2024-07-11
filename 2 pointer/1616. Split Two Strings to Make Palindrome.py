from typing import List 

class Solution:
    def _is_p(self, s):
        return s == s[::-1]
    
    def _solve(self, a, b):
        # wlog, a[1, i] & b[i + 1, n]
        # 贪心，枚举，能用则用，先把能拼凑的凑起来
        i = 0; j = len(a) - 1
        while i <= j and a[i] == b[j]: # 移动至第一不合法的区间 [i, j]
                                       #, 如果 a, b 有一个可以用，即合法
            i += 1
            j -= 1
        return self._is_p(a[i: j + 1]) or self._is_p(b[i: j + 1])
        
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self._solve(a, b) or self._solve(b, a)
                    
def main():
    solution = Solution()  
    a = "ulacfd"; b = "jizalu"
    out = solution.checkPalindromeFormation(a, b)
    print(out) 

if __name__ == "__main__":
    main()
