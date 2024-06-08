
from typing import List 
from collections import deque

class Solution: 
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: 
        candidates = sorted(candidates) 
        ans = []
        print(candidates)
        def dfs(id, cur, sum):  
            if sum == target:
                ans.append(cur.copy())
                return 

            if id >= len(candidates) or sum > target: 
                return 
 
            for i in range(id, len(candidates)): # 枚举这个坑, i.e. dfs(), 填 [id, len) 中的哪一个

                if i > id and candidates[i] == candidates[i - 1]: continue # 已经填过一样的了
                
                dfs(i + 1, cur + [candidates[i]], sum + candidates[i]) 

        dfs(0, [], 0)  
        # bfs
        ans = []
        candidates = sorted(candidates) 

        q = deque()  
        def bfs():
            while q:
                id, cur, sum = q.popleft()
                if sum == target: ans.append(cur)

                if sum > target: continue 
                
                for i in range(id, len(candidates)):  
                    if i > id and candidates[i] == candidates[i - 1]: continue 
                    q.append((i + 1, cur + [candidates[i]], sum + candidates[i])) # 维持下一个dfs在填的坑可选的信息 [id + 1, len)
        for i, val in enumerate(candidates):
            if i > 0 and candidates[i] == candidates[i - 1]: continue 
            q.append((i + 1, [val], val))  

        bfs()
        return ans 
    
def main(): 
    solution = Solution() 
    candidates = [10,1,2,7,6,1,5]; target = 8 
   
    out = solution.combinationSum2(candidates, target) 
    print(out) 

if __name__ == "__main__":
    main()