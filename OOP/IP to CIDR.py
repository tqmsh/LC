from math import log2
class Solution:
    def _print_binary(self, x: int):
        print(bin(x)[2:])
    def _to_binary(self, x: str):
        ans = 0
        for y in x.split('.'): ans = ans * (1 << 8) + int(y)
        return ans
    def _make(self, x, amt):
        return (f'{(x >> (32 - 8)) & (1 << 9 - 1)}.'
                f'{(x >> (32 - 8 * 2) & (1 << 9 - 1))}.'
                f'{(x >> (32 - 8 * 3)) & (1 << 9 - 1)}.'
                f'{(x >> (32 - 8 * 4)) & (1 << 9 - 1)}/{32 - int(log2(amt))}') 
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        x = self._to_binary(ip)
        ans = []
        while n:   
            amt = min(x & -x, 1 << (n.bit_length() - 1)) # 1(3)010 -> 3 -> max amt = 2 ^ 3
            ans.append(self._make(x, amt))
            n -= amt
            x += amt
        return ans
ip = "255.0.0.7"; n = 10
print(Solution().ipToCIDR(ip, n))