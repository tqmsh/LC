class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return '0'
        stk = []
        for n in num:
            while stk and stk[-1] > n and k: stk.pop(); k -= 1
            stk.append(n)
        while k: stk.pop(); k -= 1
        return "".join(stk).lstrip('0') or '0'
print(Solution().removeKdigits(num = "10", k = 2))