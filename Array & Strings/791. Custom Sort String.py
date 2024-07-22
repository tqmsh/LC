from typing import List
from collections import Counter

class Solution:   
    def customSortString(self, order: str, s: str) -> str:
        mp = {ch: ID for ID, ch in enumerate(order)}
        return ''.join(sorted(s, key = lambda x: mp.get(x, float('inf')))) # 就是说，咱目前想排序一个字叫x, lambda 就是说，有一个函数，把当前的 x 拿进来，然后给一个 rank 
    
def main():
    solution = Solution()
    
    order = "cba"; s = "abcd"
    out = solution.customSortString(order, s)
    print(out) 

if __name__ == "__main__":
    main()