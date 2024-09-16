
from typing import List 
from heapq import heappush, heappop
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        a = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))])
        ans = float('inf'); now_cost = 0
        pq = []
        for r, q in a: # 从最不浩钱 -> 最耗钱枚举，枚举连续区间，淘汰最没用的，他们必然不会卷死别人
            now_cost += q
            heappush(pq, -q)
            if len(pq) == k: 
                ans = min(ans, now_cost * r) # 这家伙需要的钱最多，肯定可以满足前面的要求
                now_cost += heappop(pq)
        return ans

def main(): 
    solution = Solution()  
    quality = [3,1,10,10,1]; wage = [4,8,2,2,7]; k = 3
    out = solution.mincostToHireWorkers(quality, wage, k) 
    print(out) 

if __name__ == "__main__":
    main()