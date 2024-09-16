class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MN = -2 ** 31; MX = 2 ** 31 - 1
        
        # Edge case 溢出 32 bit: [-2^32, 2^32)
        if dividend == MN and divisor == -1: return MX
        # if divisor == MN: return 1 if dividend == MN else 0

        # Edge case / 0
        if dividend == 0: return 0
        neg = (dividend > 0) != (divisor > 0); dividend, divisor = abs(dividend), abs(divisor)
        
        l, r = 0, dividend; ans = 0
        
        while l <= r:
            mid = l + ((r - l) >> 1) 
            if self.qmul(divisor, mid, dividend): # divisor * mid <= dividant
                ans = mid
                l = mid + 1
            else: r = mid - 1
                
        return -ans if neg else ans

    def qmul(self, a: int, b: int, x: int) -> bool: 
        ans = 0
        while b > 0:
            if b & 1:  # If b is odd
                ans += a
                if ans > x: return False
                    
            b >>= 1  
            a += a 
        return True

    def qmul_OG(a: int, b: int, mod: int) -> int: # 老师的本来长这样
        ans = 0
        while b:
            if b % 2 == 1: ans = (ans + a) % mod 
            b //= 2
            a = (a + a) % mod
        return ans

def test_cases():
    sol = Solution()
    cases = [ 
        (1, -2**31),           # Expect -2**31 
    ]

    for dividend, divisor in cases:
        print(f"dividend: {dividend}, divisor: {divisor}, result: {sol.divide(dividend, divisor)}")

test_cases()