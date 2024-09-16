
from typing import List 
from heapq import heappush, heappop
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        t = 1; ans = 0
        # sort 模版 
        courses.sort(key=lambda x: x[1]) 
        # heapq 模版
        pq = []
        
        for x in courses:
            nt = t + x[0]
            if pq: mx_duration_seen = -pq[0]
            if nt - 1 <= x[1]:
                heappush(pq, -x[0])
                t = nt
                ans += 1
            # t 能小则小
            elif pq and mx_duration_seen > x[0] and nt - mx_duration_seen - 1 <= x[1]: # 撤回以前最耗时间的, 看看能不能把 t 变的最优
                heappop(pq) # 撤回以前的，学习目前的
                nt -= mx_duration_seen 
                t = nt
                heappush(pq, -x[0])

        return ans 

        # 操作尊重无后效, 每个状态都是之前状态的一个计算结果

def main(): 
    solution = Solution()  
    courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
   
    out = solution.scheduleCourse(courses) 
    print(out) 

if __name__ == "__main__":
    main()