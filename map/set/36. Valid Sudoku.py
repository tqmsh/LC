from typing import List 
class Solution: 
    def isValidSudoku(self, board):
        # 不准重复的信息
        vis = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                                   # 到j 了顺序翻一下，是确保俩地址不同，不会互相干扰, 
                                   # i,e, (1, 1), (1, 1)，只要一个是 (i, b[][]), 一个是 (b[][], j)，地址不一样就是不一样
                    vis += [(i, board[i][j]), (j, board[i][j]), (i // 3, j // 3, board[i][j])]

        print(vis)
        return len(vis) == len(set(vis))
def main():
    solution = Solution()   
    board = [['.','.'],['.','1']]
    out = solution.isValidSudoku(board)
    print(out) 

if __name__ == "__main__":
    main()
