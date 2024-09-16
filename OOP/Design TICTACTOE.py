class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.cnt = [[0] * ((n << 1) + 2) for _ in range(2 + 1)]
    
    def move(self, i: int, j: int, x: int) -> int:
        n = self.n
        # 独立标记方法 [0, n) 给 row, [n, 2n) 给 col, 2n 给 ⇘, 2n + 1 给 ⇗
        self.cnt[x][i] += 1
        self.cnt[x][j + n] += 1
        if i == j: self.cnt[x][n << 1] += 1
        if i + j == n - 1: self.cnt[x][(n << 1) + 1] += 1

        for y in [i, j + n, n << 1, (n << 1)+ 1]:  
            if self.cnt[x][y] == n: return x
        return 0
    

def test_tic_tac_toe():
    game = TicTacToe(3)
    print(game.move(0, 0, 1))  # Player 1 moves at (0, 0)
    print(game.move(0, 1, 2))  # Player 2 moves at (0, 1)
    print(game.move(1, 1, 1))  # Player 1 moves at (1, 1)
    print(game.move(1, 0, 2))  # Player 2 moves at (1, 0)
    print(game.move(2, 2, 1))  # Player 1 moves at (2, 2)
    # Player 1 should win with a diagonal [0,0] -> [1,1] -> [2,2]

test_tic_tac_toe()