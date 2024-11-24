from typing import List
from queue import PriorityQueue

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: -x[0])
        
        vis = set()  
        heap = PriorityQueue()  
        tot = 0 
        
        # 枚举可能的情况，让 ans 最大化只有两种情况（1）最大化 Σ Profit（2）最大化 Σ # category ^ 2，先做 (1) ，(2) 在 (1) 基础上最大化，打擂台

        # 贪心：从大到小枚举，能用则用
        # （1）最大化 Σ Profit
        for i in range(k):
            profit, category = items[i]
            if category in vis: heap.put(profit)    
            else: vis.add(category)   
            tot += profit  
        ans = tot + len(vis) ** 2
        
        #（2）最大化 Σ # category ^ 2
        for i in range(k, len(items)):
            profit, category = items[i]
            # 无后效性，前面的决定做就做了，现在反悔只可能更优秀，因为以后也选不了了（后面的数字都更小）
            if category not in vis and not heap.empty(): 
                vis.add(category)
                tot = tot - heap.get() + profit
                ans = max(ans, tot + len(vis) ** 2)  # 能增加则增加
        return ans
