from heapq import heappush, heappop, heapreplace, merge
class MedianFinder:
    def __init__(self): self.q1 = []; self.q2 = []
    def _add_num(self, x):
        heappush(self.q1, -x)  
        # (1) 维持不重叠性
        if self.q1 and self.q2 and -self.q1[0] > self.q2[0]: heappush(self.q2, -heappop(self.q1)) # 用 heappop 维持排序性质 
        
        # (2) 维持不对称性
        if abs(len(self.q1) - len(self.q2)) > 1:
            f = 0
            if len(self.q2) > len(self.q1): 
                self.q1, self.q2 = self.q2, self.q1 # wlog, q1 长 
                f = 1
            heappush(self.q2, -heappop(self.q1))
            if f: self.q1, self.q2 = self.q2, self.q1
    def findMedian(self): 
        if len(self.q1) > len(self.q2): return -self.q1[0]
        elif len(self.q1) < len(self.q2): return self.q2[0]
        else: return (-self.q1[0] + self.q2[0]) / 2
mf = MedianFinder()
mf._add_num(2)
mf._add_num(2)
mf._add_num(2)
mf._add_num(2)
assert mf.findMedian() == 2, "Test case 7 failed"
