from typing import List 
from collections import deque
from itertools import accumulate
class Solution:
    def _dfs(self, x, path: str, path_num: int, path_tot: int, target: int, ans: List[str], num: str):
        if x == len(num): 
            if path_tot == target: ans.append(path)
            return 
        
        # 可能性剪枝 a, b, c, d; a + b (cd) => a + b * c * d
        if path_num > 0 and path_tot - path_num + path_num * int(num[x:]) < target: return  
        
        # 拿当前数字
        for nx in range(x + 1, len(num) + 1): 
            if nx - 1 > x and num[x] == '0': break  # leading zeros 
            tmp = int(num[x: nx])# [x -> nx） 的过程
            if x == 0: 
                self._dfs(nx, str(tmp), tmp, tmp, target, ans, num)
                continue
            self._dfs(nx, path + '+' + str(tmp), tmp, path_tot + tmp, target, ans, num)
            self._dfs(nx, path + '-' + str(tmp), -tmp, path_tot - tmp, target, ans, num)
            self._dfs(nx, path + '*' + str(tmp), tmp, path_tot - path_num + path_num * tmp, target, ans, num) 
                

    def addOperators(self, num: str, target: int) -> List[str]: 
        ans = []
        self._dfs(0, "", 0, 0, target, ans, num)
        return ans 
    
def main(): 
    solution = Solution() 
    num = "123456789"; target = 45
   
    out = solution.addOperators(num, target) 
    print(out) 

if __name__ == "__main__":
    main()