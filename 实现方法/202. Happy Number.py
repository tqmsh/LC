from typing import List
from collections import Counter

class Solution: 
    def isHappy(self, n: int) -> bool:
        # set 模版
        vis = set()
        while(n != 1):
            if n in vis: return False # 环
            vis.add(n) 

            # 数字位 模版
            n = sum([int(i) ** 2 for i in str(n)]) 
        return True
    
def main():
    solution = Solution() 
    out = solution.isHappy(19)
    print(out) 

if __name__ == "__main__":
    main()