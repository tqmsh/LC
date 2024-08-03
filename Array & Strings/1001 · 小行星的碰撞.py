from typing import List
from collections import Counter

class Solution: 
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = [] # 维持还活着的
        
        for x in asteroids: 
            while stk and x < 0 < stk[-1]: # 把炸的跳掉，即占最后向右，x向左边
                if stk[-1] < -x: stk.pop() # x 炸碎一个对面的 
                elif stk[-1] == -x: # x 炸碎对面的，但是自己也不能继续了
                    stk.pop() 
                    break
                else: break # 自己不能继续了
            else: stk.append(x)  
        return list(stk)
def main():
    solution = Solution()
    nums = [-2,-1,1,2]
    out = solution.asteroidCollision(nums)
    print(out) 

if __name__ == "__main__":
    main()