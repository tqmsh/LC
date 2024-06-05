# Question:
# Given a Minesweeper game board and a click position, reveal the board according to Minesweeper rules, updating it based on the click's result.

# Input:
# The input is an m x n character matrix representing the game board, where each cell can
# be 'M' (mine), 'E' (empty), 'B' (blank), or a digit ('1' to '8'), and a list representing the
# click position. This input defines the initial state of the game and the user's action.

# Output:
# The output is the updated board after processing the click, revealing cells according to
# the game rules and reflecting the new state of the board.
from collections import deque
from typing import List 
from collections import deque

class Solution: 
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]: 
        # 走图 vis 模版
        q = deque()
        vis = set() 
        def check(x, y): 
            # 没有越界，没有走过，不是障碍 (这一点以后特判)
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]): return 0  
            if (x, y) in vis: return 0 
            return 1 
        
        def bfs():
            dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
            while q:
                x, y = q.popleft()  
                if (x, y) not in vis: vis.add((x, y))  # 进队出有很多种情况 - 出队只有一种
                
                # 进门后, 1) 用旁边的信息填自己颜色, 2）扩散，注：x, y 的信息不用在被扩散时(进队)全部订好，也可以出队后慢慢定，只要进队时录一下 vis 即可
                mineCnt = 0
                for dx, dy in dir: 
                    nx, ny = x + dx, y + dy 
                    if check(nx, ny) and board[nx][ny] == 'M':
                        mineCnt += 1
                # (2) 扩散
                if mineCnt > 0: 
                    board[x][y] = chr(ord('0') + mineCnt)
                else:
                    board[x][y] = 'B'
                    for dx, dy in dir: 
                        nx, ny = x + dx, y + dy 
                        if check(nx, ny) and board[nx][ny] == 'E':
                            q.append((nx, ny))
                            vis.add((nx, ny)) 
                     
        # 把所有的出发点都放到 q 里面 
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        elif board[click[0]][click[1]] == 'E': 
            q.append((click[0], click[1])) 
            bfs()    
        return board

 
def display_grid(array):
    for row in array:
        for element in row:
            print(f"{element}\t", end="")
        print()  # Newline after each row
    print('--------------------------------------------------------') 
def main(): 
    solution = Solution() 
    board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
    click = [3, 0]
    display_grid(board)
    out = solution.updateBoard(board, click)
    display_grid(out)
    print(out) 

if __name__ == "__main__":
    main()