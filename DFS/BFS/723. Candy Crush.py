from typing import List
class Solution:
    def _mark(self, board, run): 
        for i in range(len(board)):
            for j in range(len(board[0])):
                # In place horizontal mark
                if j + 2 < len(board[0]) and board[i][j] and abs(board[i][j]) == abs(board[i][j + 1]) and abs(board[i][j]) == abs(board[i][j + 2]): 
                    run[0] = 1
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j + 2])
                # In place vertical mark
                if i + 2 < len(board) and board[i][j] and abs(board[i][j]) == abs(board[i + 1][j]) and abs(board[i][j]) == abs(board[i + 2][j]): 
                    run[0] = 1
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i + 2][j])


    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        run = [1]
        while run[0]:
            run[0] = 0
            self._mark(board, run)
            if run[0]:
                # Gravity
                for j in range(len(board[0])):
                    # Where board is being updated, never raise faster than i
                    k = len(board) - 1
                    # Fall
                    for i in range(len(board) - 1, -1, -1):
                        if board[i][j] > 0:
                            # Will Fall
                            board[k][j] = board[i][j]
                            k -= 1
                    # Clean map
                    while k >= 0:
                        board[k][j] = 0
                        k -= 1
        return board
board = [
    [1, 1, 1],
    [2, 0, 0],
    [0, 0, 2]
]
print(Solution().candyCrush(board))