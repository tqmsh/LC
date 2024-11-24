from typing import List
from collections import deque
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool: 
        stk = deque() # stk[0], stk[-1], 表示一回合，如果双方都是从两边开始往里消，谁赚谁亏
        for x in nums:
            # 贪心: 从必然入手, 能用则用，必然赚的情况

            # 如果 A 选 x 得到 x 好处，然后 B 必然选 Interaction stk[-1] 因为即使 A 后面选 stk[-2] 好处，B 也是赚的 
            if len(stk) >= 2 and x <= stk[-1] and stk[-1] > stk[-2]: 
                x = stk[-2] + x - stk[-1]
                stk.pop()   
                stk.pop()  
            stk.append(x)
        
        ans = 0  
        flag = 1   
        # 贪心: 一步一步走，每一步都得最优
        while stk:  
            # 从两边向内消除，哪一种最优？这个消除过程，如果是 max 的话，则是必然的，因为另外一边没这个好处
            if flag: ans += max(stk[0], stk[-1])   
            else: ans -= max(stk[0], stk[-1])   
                 
            if stk[0] > stk[-1]: stk.popleft()   
            else: stk.pop()   
            flag ^= 1  
        return ans >= 0