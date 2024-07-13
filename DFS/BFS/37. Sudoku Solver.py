# Question:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.

# Input:
# The input is a string of digits from 2 to 9, where each digit maps to a set of letters as on
# a telephone keypad. This input defines the digits whose corresponding letter combinations
# need to be found.

# Output:
# The output is a list of strings, where each string represents a possible letter combination
# that the input digits could represent, reflecting all possible combinations.

from typing import List 
from collections import deque

class Solution: 
    def _check(self, cur_board, step_i, step_j, val):
        if val in cur_board[step_i]: return 0 # 横的不重复
        if val in [cur_board[i][step_j] for i in range(9)]: return 0 # 竖的不重复
        # 3 x 3 不重复
        for i in range((step_i // 3) * 3, (step_i // 3) * 3 + 3): # 把 cur_i 降至当前 3x3 的i起始点
            for j in range((step_j // 3) * 3, (step_j // 3) * 3 + 3): 
                if val == cur_board[i][j]: return 0
        return 1
    def _dfs(self, cur_board, step_i, step_j): 
        # step: 当前在填第几个坑
        if step_j == len(cur_board[0]): # 出门后录，进队/门方法很多，出队/门就一种，好写  
            step_i += 1
            step_j = 0
        if step_i == len(cur_board): # 1 - n 的坑都填好了，找到了一种方案
            return 1 # 已经找到了，可以结束了
        if cur_board[step_i][step_j] == '.':   
            for i in range(1, 10): # 枚举这个坑填啥
                if self._check(cur_board, step_i, step_j, str(i)):
                    cur_board[step_i][step_j] = str(i) 
                    if self._dfs(cur_board, step_i, step_j + 1): return 1
                    cur_board[step_i][step_j] = '.'
        else: 
            return self._dfs(cur_board, step_i, step_j + 1,)
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 如果 _check 非常难满足，即剪枝会很恨，可能可以满足  
        self._dfs(board, 0, 0)
        return board

def main(): 
    solution = Solution() 
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    out = solution.solveSudoku(board) 
    print(out) 

if __name__ == "__main__":
    main()