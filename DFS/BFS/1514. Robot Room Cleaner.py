from typing import List, Set, Tuple

class Robot:
    def __init__(self, room: List[List[int]], sx: int, sy: int):
        self.room = room
        self.x = sx
        self.y = sy
        self.dirx = [-1, 0, 1, 0] # up, right, down, left
        self.diry = [0, 1, 0, -1]
        self.d = 0  

    def move(self) -> bool:
        nx = self.x + self.dirx[self.d]
        ny = self.y + self.diry[self.d]

        if 0 <= nx < len(self.room) and 0 <= ny < len(self.room[0]) and (self.room[nx][ny] == 1 or self.room[nx][ny] == 2):
            self.x = nx
            self.y = ny
            return True
        return False

    def turnLeft(self):
        self.d = (self.d - 1) % 4

    def turnRight(self):
        self.d = (self.d + 1) % 4

    def clean(self):
        self.room[self.x][self.y] = 2   
        print(f"Cleaned cell: ({self.x}, {self.y})")   
class Solution:
    def _check(self, x: int, y: int, vis: Set[Tuple[int, int]], robot: Robot) -> bool:
        if (x, y) in vis: 
            return False
        if robot.move(): # move() 同步 nx = x + d
            return True
        return False

    def _go_back(self, robot: Robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def _dd(self, robot):
        for row in robot.room: print(row)
    def _dfs(self, x: int, y: int, d: int,  vis: Set[Tuple[int, int]], robot: Robot):
        vis.add((x, y))
        robot.clean() 
        self._dd(robot)
        
        dirx = [-1, 0, 1, 0]
        diry = [0, 1, 0, -1]

        for i in range(4):
            nd = (d + i) % 4 # 同步机器人目前方向，确保当 i = 0 时，机器人直走
            nx = x + dirx[nd]
            ny = y + diry[nd] 
            print(f"Trying to move to: ({nx}, {ny}), {nd}, from {x}, {y}")  # Debug statement 
            if self._check(nx, ny, vis, robot): # 所有的 x, y 操作，机器人都必须同步
                self._dfs(nx, ny, nd, vis, robot)
                self._go_back(robot)
            robot.turnRight() # 同步 i += 1 换方向 

    def cleanRoom(self, row: int, col: int, robot: Robot):
        vis = set()
        self._dfs(row, col, 0, vis, robot)
        return robot.room
def main():
    room = [
        [1,1,1,1,1,0,1,1],
        [1,1,1,1,1,0,1,1],
        [1,0,1,1,1,1,1,1],
        [0,0,0,1,0,0,0,0],
        [1,1,1,1,1,1,1,1]
    ] 
    row, col = 0, 1
    robot = Robot(room, row, col)
    solution = Solution()
    cleaned_room = solution.cleanRoom(row, col, robot)
    for row in cleaned_room:
        print(row)
if __name__ == "__main__":
    main()