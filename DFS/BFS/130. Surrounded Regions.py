class Solution:
    def _check(self, i, j, board): return 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O'
    def _dfs(self, x, y, board):
        board[x][y] = 'o'  
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if self._check(x + dx, y + dy, board):
                self._dfs(x + dx, y + dy, board)
    
    def solve(self, board):
        for i in range(len(board)):
            if board[i][0] == 'O': self._dfs(i, 0, board) 
            if board[i][len(board[0]) - 1] == 'O': self._dfs(i, len(board[0]) - 1, board)
            
        for j in range(len(board[0])):
            if board[0][j] == 'O': self._dfs(0, j, board) 
            if board[len(board) - 1][j] == 'O': self._dfs(len(board) - 1, j, board)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'o': board[i][j] = 'O' 
                else: board[i][j] = 'X'
class Solution:
    def _check(self, x, y, vis, board, ans):  
        if not(0 <= x < len(board) and 0 <= y < len(board[0])):
            ans[0] = 1
            return False
        if vis[x][y] or board[x][y] != 'O':
            return False
        return True
        
    def _dfs(self, x, y, vis, board, ans, col): 
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        vis[x][y] = col
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if self._check(nx, ny, vis, board, ans):
                self._dfs(nx, ny, vis, board, ans, col)
            
    def _fill(self, x, y, vis, board, col):
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        board[x][y] = 'X'
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'O' and vis[nx][ny] == col:
                self._fill(nx, ny, vis, board, col)
            
    def solve(self, board):  
        vis = [[0] * len(board[0]) for _ in range(len(board))]
        col = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and not vis[i][j]:
                    col += 1
                    ans = [0]
                    self._dfs(i, j, vis, board, ans, col)
                    if not ans[0]:  # If surrounded
                        self._fill(i, j, vis, board, col)
        return board

# Create an instance of Solution
solution = Solution()

# Define the board
board = [['X']]

# Call the solve method on the instance
result = solution.solve(board)

# Print the result
print(result)
