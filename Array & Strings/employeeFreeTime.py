from typing import List
class Interval:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Interval({self.start}, {self.end})"
class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]):
        ans: List[Interval] = []
        d = []
        # 差分
        for intervals in schedule:
            for interval in intervals:
                d.append([interval.start, 1])
                d.append([interval.end, -1])
        # 时间点考后的排前面，先结束再开始
        d.sort(key=lambda x: (x[0], -x[1]))

        # 离散化，枚举关键信息
        cnt = f = 0
        for idx, val in d:
            cnt += val
            if cnt == 0:
                ans.append(Interval(idx))
                f = 1
            elif f:
                ans[-1].end = idx
                f = False
        ans.pop()
        return ans
    
schedule = [
    [Interval(1, 3), Interval(6, 7)],
    [Interval(2, 4)],
    [Interval(2, 5)], [Interval(9, 12)]
]
free_times = Solution().employeeFreeTime(schedule)
print(free_times)