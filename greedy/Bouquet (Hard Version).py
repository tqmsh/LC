from typing import List

class Flower:
    def __init__(self, petals: int, quantity: int): 
        self.petals = petals  
        self.quantity = quantity    
    def __lt__(self, other: 'Flower'): 
        return self.petals < other.petals 
    def __repr__(self): 
        return f'({self.petals}, {self.quantity})'

def max_petals(flowers: List[Flower], m):
    flowers.sort(); ans = 0; n = len(flowers) 

    # 特殊情况处理：只有一种花的情况
    if n == 1:
        amt_fir = min(m // flowers[0].petals, flowers[0].quantity)
        ans = flowers[0].petals * amt_fir
        return ans

    # 贪心，(区间)，能一起则一起，枚举连续区间, 因为最多差一，所以就枚举一对，因为最多就一对做答案
    for i in range(n - 1):
        fir = flowers[i]; sec = flowers[i + 1]

        # Case 1: fir & sec 不能共存
        if sec.petals != fir.petals + 1:
            amt_fir = min(m // fir.petals, fir.quantity) # 用 m 最多能买 fir / sec 各多少
            amt_sec = min(m // sec.petals, sec.quantity)
            tot_fir = amt_fir * fir.petals # 最多能买多少 petals 
            tot_sec = amt_sec * sec.petals
            ans = max(ans, tot_fir, tot_sec) # 取更优的 
            continue
        
        # Case 2: fir & sec 能共存 
        # Case 2.1: 能同时买所有的 fir & sec
        tot_fir = fir.quantity * fir.petals
        tot_sec = sec.quantity * sec.petals
        if tot_fir + tot_sec <= m: 
            ans = max(ans, tot_fir + tot_sec)
            continue

        # Case 2.2: 不能同时购买所有的 fir & sec
        # 贪心：一步一步走，每一步都得最优
        amt_fir = min(m // fir.petals, fir.quantity) #尽可能多买 fir 。。。 
        tot_fir = amt_fir * fir.petals
        amt_sec = min((m - tot_fir) // sec.petals, sec.quantity)
        tot_sec = amt_sec * sec.petals
        tot = tot_fir + tot_sec # fir & sec 目前总价值
        left_sec = sec.quantity - amt_sec
        left_m = m - tot # 剩余价钱

        # 。。。 然后逐个用 sec 替换掉 fir，直到无法替换
        if amt_fir > 0 and left_sec > 0 and left_m > 0:
            # 存在购买fir   # 存在库存sec      # 有剩余钱去换购

            # 每一次 sec 替换 fir, tot += 1, 因为 |fir - sec| <= 1 & fir != sec => fir + 1 = sec
            exchanges = min(amt_fir, left_sec, left_m)
            tot += exchanges

        ans = max(ans, tot)
    
    return ans

# Test cases
flowers1 = [Flower(1, 2), Flower(2, 2), Flower(3, 1)]  # Test case 1
m1 = 10  # Budget
print(max_petals(flowers1, m1))  # Expected output: 7

flowers2 = [Flower(206, 3), Flower(207, 4), Flower(1000, 1)]  # Test case 2
m2 = 1033  # Budget
print(max_petals(flowers2, m2))  # Expected output: 1033

flowers3 = [Flower(4, 1), Flower(2, 2), Flower(7, 1), Flower(5, 3), Flower(6, 1), Flower(1, 7)]  # Test case 3
m3 = 20  # Budget
print(max_petals(flowers3, m3))  # Expected output: 19

flowers4 = [Flower(239, 12), Flower(30, 13123), Flower(610, 112), Flower(122, 1456), Flower(24, 124), Flower(40, 100), Flower(8, 123), Flower(2, 10982)]  # Test case 4
m4 = 100000  # Budget
print(max_petals(flowers4, m4))  # Expected output: 999990 