from typing import List
from collections import Counter

class Solution: 
    def get_different_number(self, arr):
        s = set(); j = 0 # set 是 hash table 的 abstraction, add & check membership 都是 O(1)
        for num in arr:
            s.add(num)
            while j in s:
                j += 1 # 爬楼梯，第一个不合法，即第一个楼梯断层处 
        return j   
# s_b[mx[0]:mx[1] + 1].decode()

    
def main():
    solution = Solution()
    arr = [0, 2, 1, 3, 5]
    out = solution.get_different_number(arr)
    print(out) 

if __name__ == "__main__":
    main()