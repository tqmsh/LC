from typing import List

class Solution:    
    def _dfs1(self, i, path_j, path_d1, path_d2, path_space, ans, n):
        if i == n:
            tmp = []
            for x in path_space: 
                tmp.append('.' * x + 'Q' + '.' * (n - x - 1))
            ans.append(tmp)
            return
        avail = ((1 << n) - 1) & (~ (path_j | path_d1 | path_d2))
        while avail:
            pos = avail & (-avail)
            avail = avail & (avail - 1)
            self._dfs1(i + 1, path_j | pos, (path_d1 | pos) << 1, (path_d2 | pos) >> 1, path_space + [bin(pos).count('0') - 1], ans, n)

    def _dfs2(self, i, path_j, path_d1, path_d2, ans, n):
        if i == n:
            ans[0] += 1
            return
        avail = ((1 << n) - 1) & (~ (path_j | path_d1 | path_d2))
        while avail:
            pos = avail & (-avail)
            avail = avail & (avail - 1)
            self._dfs2(i + 1, path_j | pos, (path_d1 | pos) << 1, (path_d2 | pos) >> 1, ans, n)

    def total_n_queens(self, n: int) -> int:
        ans = [0]
        self._dfs2(0, 0, 0, 0, ans, n)
        return ans[0]

    def solve_n_queens(self, n: int) -> List[List[str]]:
        ans = []
        self._dfs1(0, 0, 0, 0, [], ans, n)
        return ans
        
def main():
    solution = Solution() 
    n = 4 
    count = solution.total_n_queens(n)
    print("Total number of solutions:", count) 
     
    solutions = solution.solve_n_queens(n)
    for solution in solutions:
        for row in solution: print(row) 
        print() 
    
if __name__ == "__main__":
    main()
