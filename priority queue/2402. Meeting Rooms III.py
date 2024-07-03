
from typing import List 
from heapq import heappush, heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_pq = [i for i in range(n)] # free[0]: 最小的 id
        busy_pq = [] # busy[0]: 最小的 e
        cnt = [0] * n
        meetings.sort()  

        for s, e in meetings:
            # 模拟，更新占用的屋子 
            while busy_pq and busy_pq[0][0] <= s: # busy: [s, e), busy's e 可以用; 答案枚举
                _, ID = heappop(busy_pq)
                heappush(free_pq, ID)

            # 如果有空出的屋子，给它
            if free_pq:
                ID = heappop(free_pq)
                heappush(busy_pq, (e, ID))

            # 如果没有空出的屋子，把最早结束的给它，顺便更新他的结束时间
            else: 
                ee, ID = heappop(busy_pq)
                heappush(busy_pq, (ee + e - s, ID))
            
            cnt[ID] += 1
        print(cnt)
        # index 模版
        return cnt.index(max(cnt))

def main(): 
    solution = Solution()  
    meetings = [[0,10],[1,5],[2,7],[3,4]] 
   
    out = solution.mostBooked(2, meetings) 
    print(out) 

if __name__ == "__main__":
    main()