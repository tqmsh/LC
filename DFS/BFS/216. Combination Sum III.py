
from typing import List 
from collections import deque

class Solution: 
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 防重 模版 
        ans = [] 
        def dfs(id, cur, sum):  
            if len(cur) == k and sum == n: 
                ans.append(cur.copy())
                return 

            if id > 9 or sum > n: 
                return  
            
            for i in range(id, 9 + 1): # 枚举这个坑, i.e. dfs(), 填 [id, len) 中的哪一个  
                dfs(i + 1, cur + [i], sum + i) 

        dfs(1, [], 0)  

        # bfs
        # ans = [] 

        # q = deque()  
        # def bfs():
        #     while q:
        #         id, cur, sum = q.popleft()
        #         if len(cur) == k and sum == n: 
        #             ans.append(cur)
        #             continue

        #         if sum > n: 
        #             continue 
                
        #         for i in range(id, 9 + 1):   
        #             q.append((i + 1, cur + [i], sum + i)) # 维持下一个dfs在填的坑可选的信息 [id + 1, len)
        
        # for i in range(1, 9 + 1):
        #     q.append((i + 1, [i], i))  

        # bfs()
        # return ans 
    
def main(): 
    solution = Solution() 
    k = 9; n = 45
   
    out = solution.combinationSum3(k, n) 
    print(out) 

if __name__ == "__main__":
    main()