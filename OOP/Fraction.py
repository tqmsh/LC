from math import gcd
from collections import defaultdict
class Fraction: 
    def __init__(self, num: int, den: int): 
        if den == 0: raise ValueError('den = 0') # 🟥 /0 edge case处理
        self.num = num; self.den = den; self.simplity()
        
    def simplity(self): 
        # 数字化简
        g = gcd(self.num, self.den)
        self.num //= g; self.den //= g
        # 符号统一
        if self.den < 0: 
            self.num *= -1; self.den *= -1
        
    def toDecimal(self, precision=None) -> str: 
        ans, rem = divmod(abs(self.num), abs(self.den))
        ans = str(ans) + ("." if rem else "")
        mp = defaultdict(int)
        
        count = 0  # 追踪小数位数
        # 需要解决
        while rem and rem not in mp:
            # 如果指定了精度且已经达到，停止进一步计算
            if precision is not None and count >= precision:
                break
            # log
            mp[rem] = len(ans)
            # 下一个 0
            rem *= 10
            # 上商
            ans += str(rem // abs(self.den))
            rem %= abs(self.den) 
            count += 1  # 增加小数位数计数
        
        # 如果余数重复，我们插入括号
        if rem and (precision is None or count < precision):
            ans = ans[:mp[rem]] + '(' + ans[mp[rem]:] + ')'
        
        # 必要时添加负号
        return ('-' if self.num * self.den < 0 else "") + ans

# 测试
def test_fraction():
    f3 = Fraction(1, 3)
    print(f3.toDecimal())

test_fraction()
