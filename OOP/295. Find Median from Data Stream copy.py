from typing import List
from heapq import heappush, heappop
from collections import defaultdict
class MedianFinder:
    def __init__(self):
        self.small, self.large = [], [] 
        self.lazy = defaultdict(int); self.balance = 0 # balance = len(large) - len(small)
    def add(self, x):
        if not self.small or x <= -self.small[0]: heappush(self.small, -x); self.balance -= 1 
        else: heappush(self.large, x); self.balance += 1
        self.rebalance()
    def rebalance(self):
        while self.balance < 0: heappush(self.large, -heappop(self.small)); self.balance += 2
        while self.balance > 0: heappush(self.small, -heappop(self.large)); self.balance -= 2
    def remove(self, x):
        self.lazy[x] += 1
        if x <= -self.small[0]: self.balance += 1 # len(small) - 1
        else: self.balance -= 1 
        self.rebalance()
        self.push_down() # 记账法
    def push_down(self): 
        while self.small and self.lazy[-self.small[0]] > 0: # [xxxxxx( -small[0] )][(large[0])xxxxxx], 
            self.lazy[-self.small[0]] -= 1; heappop(self.small) 
        while self.large and self.lazy[self.large[0]] > 0:
            self.lazy[self.large[0]] -= 1; heappop(self.large)
    def find_median(self): 
        if self.balance == 0: return (-self.small[0] + self.large[0]) / 2 
        elif self.balance < 0: return -self.small[0] 
        else: return self.large[0] 

class Solution:
    def medianSlidingWindow(self, xs: List[int], k: int) -> List[float]:
        ans = []
        median_finder = MedianFinder()  
        for i, x in enumerate(xs): # [0, i]
            median_finder.add(x) 
            if i >= k: median_finder.remove(xs[i - k]) # len >= k + 1, i - 0 + 1 >= k = 1, i >= k  
            if i >= k - 1: ans.append(median_finder.find_median()) # len >= k, i - 0 + 1 >= k, i >= k - 1
        return ans
    
nums = [1,2,3,4,2,3,1,4,2]; k = 3
print(Solution().medianSlidingWindow(nums, k))