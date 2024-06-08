
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
            if nt - 1 <= x[1]:
                heappush(pq, -x[0])
                t = nt
                ans += 1
            elif pq and pq[0] < -x[0] and nt + (pq[0]) - 1 <= x[1]: 
                # 无后效, 某阶段的状态一旦确定，则此后过程的决策不再受此前各种状态及决策的影响
                # 现在如果决定把以前最耗时间的拉出来 （如果有帮助的话），以后不受其影响，因为以前的课不能被重新学习，所以以后处理的也是一样的
                nt += heappop(pq) # 拿最靠左
                t = nt
                heappush(pq, -x[0])

        return ans
 


def main(): 
    solution = Solution()  
    courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
   
    out = solution.scheduleCourse(courses) 
    print(out) 

if __name__ == "__main__":
    main()