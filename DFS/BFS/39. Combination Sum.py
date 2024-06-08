
from typing import List 
from collections import deque

class Solution:
    # 子集枚举 2^n 模版
    # 有n个坑，每个坑可以种萝卜，或者不种萝卜，请问有多少种不同的种植方法? 有n个坑，每个坑可以填0/1， 请打印所有的方案; 
    # n <= 25; [1, x]个坑，每个填 [l, r], 无序，不重复
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # ans = []
        
        # def dfs(i, cur, sum): 
        #     # 最优性剪枝， 如果不可能再优了，就没必要跑了
        #     # 可行性剪枝， 如果不存在方法，跑了也没意义，就不跑了

        #     if sum == target:
        #         ans.append(cur.copy())
        #         return 

        #     if i >= len(candidates) or sum > target: 
        #         return
         
        #     cur.append(candidates[i])
 
        #     # 完全背包 
        #     dfs(i, cur, sum + candidates[i]) # 空出一件的体积, 剩下的体积依旧在前i件种选择最优
        #     cur.pop() 
        #     dfs(i + 1, cur, sum) # 一件都不要

        # dfs(0, [], 0) 

        # bfs
        ans = []
        q = deque()  
        def bfs():
            while q:
                id, cur, sum = q.popleft()
                if sum > target: continue
                    
                # 进队出有很多种情况 - 出队只有一种; 这次选择出出队时判断
                if sum == target: ans.append(cur)
                
                for i in range(id, len(candidates)): # 只往前看，边枚举边计算，防重 
                    q.append((i, cur + [candidates[i]], sum + candidates[i]))
        for id, val in enumerate(candidates):
            q.append((id, [val], val))  
        bfs()
        return ans 
    
def main(): 
    solution = Solution() 
    candidates = [2,3,6,7]; target = 7  
    out = solution.combinationSum(candidates, target) 
    print(out) 

if __name__ == "__main__":
    main()