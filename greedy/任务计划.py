from typing import List
from collections import Counter, defaultdict 
class Solution:
    def leastInteral(self, tasks: List[int], n: int) -> int:
        # Case I: 存在 cd
        cnts = list(Counter(tasks).values())
        mx = max(cnts)
        num_mx = cnts.count(mx)
        
        # 所需时间被最值所限制，最值所需的等待时间足够支撑别的次值

        # (n + 1) * (mx - 1): cd -> cd -> cd -> cd -> cd -> cd 
        # 足够支撑所有的, i.e. A -> B -> cd -> A -> B -> cd  
        # + num_mx: 最后的结尾， i.e. A -> B -> cd -> A -> B -> cd -> A -> B

        # Case II: 不存在 cd，即 len(tasks)
        return max(len(tasks), (n + 1) * (mx - 1) + num_mx)

print(Solution().leastInteral(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'D', 'E', 'F'], 2))
        # a -> cd -> cd -> a -> cd -> cd -> a
        # a -> b -> cd -> a -> b -> cd -> a -> b

