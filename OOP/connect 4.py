from enum import Enum
from typing import List
from collections import defaultdict

def _check(x: int, y: int, grid: List[List[int]], req: int) -> bool:
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return 0  
    if grid[x][y] != req: return 0
    return 1

class GridPos(Enum): EMPTY = 0; YELLOW = 1; RED = 2

class Grid:
    def __init__(self, n, m): self._n = n; self._m = m; self._grid = None; self.initGrid()
    def initGrid(self): self._grid = [[GridPos.EMPTY for _ in range(self._m)] for _ in range(self._n)]
    def getGrid(self): return self._grid
    def getM(self): return self._m
    def placePiece(self, j, col):
        if j < 0 or j >= self._m: raise ValueError('bad j')
        if col == GridPos.EMPTY: raise ValueError('bad col')
        for i in range(self._n - 1, -1, -1):
            if self._grid[i][j] == GridPos.EMPTY: self._grid[i][j] = col; return i
    def checkWin(self, req, x, y, col):
        dirx = [0, 0, -1, 1]; diry = [-1, 1, 0, 0]
        for i in range(4):
            cnt = 0
            for j in range(-req + 1, req):
                nx = x + dirx[i] * j; ny = y + diry[i] * j
                if _check(nx, ny, self._grid, col): cnt += 1
                else: cnt = 0
                if cnt == req: return 1
        return 0

class Player:
    def __init__(self, name, col): self._name = name; self._col = col
    def getName(self): return self._name
    def getCol(self): return self._col

class Game:
    def __init__(self, grid: Grid, req, targetScore):
        self._grid = grid; self._req = req; self._targetScore = targetScore
        self._players = [Player('p1', GridPos.YELLOW), Player('P2', GridPos.RED)]
        self._score = defaultdict(lambda: 0)
    def printBoard(self):
        print('Board:\n')
        grid = self._grid.getGrid()
        for r in grid:
            ans = ""
            for c in r:
                if c == GridPos.EMPTY: ans += '0'
                if c == GridPos.YELLOW: ans += 'Y'
                if c == GridPos.RED: ans += 'R'
            print(ans)
        print('')
    def playMove(self, player: Player):
        self.printBoard(); print(f"{player.getName()}'s turn")
        j = int(input(f'[0, {self._grid.getM()})'))
        i = self._grid.placePiece(j, player.getCol())
        return (i, j)
    def playRound(self):
        while 1:
            for player in self._players:
                i, j = self.playMove(player); col = player.getCol()
                if self._grid.checkWin(self._req, i, j, col): self._score[player] += 1; return player
    def play(self):
        mx = 0; winner = None
        while mx < self._targetScore:
            winner = self.playRound(); print(f'{winner.getName()} won')
            mx = max(self._score[winner], mx); self._grid.initGrid()
        print(f'{winner.getName()}')  # Corrected to call the method

grid = Grid(6, 7); game = Game(grid, 4, 2); game.play()
