from typing import List
from heapq import heappush, heappop, heapify
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        pq = [0] # abs(pq[0]): 目前最高高度
        a = []
        for x1, x2, y in buildings: a.append((x1, -y)); a.append((x2, y))
        a.sort()  
        # 离散化
        ans = []
        # sweap line 排序，即 x 从小到大枚举，先枚举入在枚举出，如果是入的话，先枚举最高的 y，如果是出的话，先枚举最低的 y
        for x, y in a: # 枚举 x
            if y < 0: # 入

                # 贪心，枚举到的第一个必然是这个 x 的最高点，如果需要画以下图，那就画
                #          - <- 开始的 y, 最高的 = 被画
                #          -
                # ---------|
                if abs(y) > abs(pq[0]): ans.append([x, abs(y)]) 
                heappush(pq, y)
            else: 
                # 退出建筑
                pq.remove(-y); heapify(pq) 

                 # 贪心，枚举到的第一个必然是这个 x 的最低点，如果需要画以下图，那就画
                # ---------|
                # ---------| <- 结束的 y, 最低的，低于这个的 = 低于所有 = 被画
                #          |
                # ---------- <- 画一个点 pq[0]

                if abs(pq[0]) < y: ans.append([x, abs(pq[0])])
        return ans

        

        
        

print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))