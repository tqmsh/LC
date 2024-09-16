from typing import List
class Direction: UP = "UP"; DOWN = "DOWN"
class Status: UP = "UP"; DOWN = "DOWN"; IDLE = "IDLE"
class Request:
    def __init__(self, lvl = 0): self._lvl = lvl
    def getLvl(self): return self._lvl
class ElevatorButton:
    def __init__(self, lvl, elevator): self._lvl = lvl; self.elevator = elevator
class ExternalRequest(Request):
    def __init__(self, lvl = 0, dir = None): super().__init__(lvl); self._dir = dir
    def getDir(self): return self._dir
class InternalRequest(Request):
    def __init__(self, lvl = 0): super().__init__(lvl)
class Elevator:
    def __init__(self, num_lvls): 
        self.buttons: List[ElevatorButton] = []; self.upStops = [0] * (num_lvls + 1)
        self.downStops = [0] * (num_lvls + 1); self.now_lvl = 1; self.status = Status.IDLE
    def insertButton(self, button: ElevatorButton): self.buttons.append(button)

    def noRequests(self, stops): return not any(stops)

    def handleExternal(self, req: ExternalRequest): # 必然停，如移则移
        if req.getDir() == Direction.UP: 
            self.upStops[req.getLvl()] = 1
            if self.noRequests(self.downStops): self.status = Direction.UP
        else:
            self.downStops[req.getLvl()] = 1
            if self.noRequests(self.upStops): self.status = Direction.DOWN
        print(self.elevatorStatusDescription())

    def handleInternal(self, req: InternalRequest): # 顺路，得停；否则不停
        if self.status == Status.UP:
            if req.getLvl() > self.now_lvl: self.upStops[req.getLvl()] = 1 
        if self.status == Status.DOWN:
            if req.getLvl() < self.now_lvl: self.downStops[req.getLvl()] = 1
        print(self.elevatorStatusDescription())

    def openGate(self): # 走
        if self.status == Status.UP: # 模拟向上
            for i in range(len(self.upStops)): # 得停
                x = (self.now_lvl + i) % len(self.upStops) # 优先查看上面的，然后查看有没有下面的楼层需要被往上接
                if self.upStops[x]: 
                    self.now_lvl = x
                    self.upStops[x] = 0
                    break
        if self.status == Status.DOWN:
            for i in range(len(self.downStops)):
                x = (self.now_lvl - i) % len(self.downStops) 
                if self.downStops[x]:
                    self.now_lvl = x
                    self.downStops[x] = 0
                    break
        print(self.elevatorStatusDescription())

    def closeGate(self): # 调整下一步的方向
        if self.status == Status.IDLE:
            if self.noRequests(self.downStops): 
                self.status = Status.UP
                return
            if self.noRequests(self.upStops):
                self.status = Status.DOWN
                return 
        elif self.status == Status.UP:
            if self.noRequests(self.upStops):
                if self.noRequests(self.downStops): self.status = Status.IDLE
                else: self.status = Status.DOWN
        elif self.status == Status.DOWN:
            if self.noRequests(self.downStops):
                if self.noRequests(self.upStops): self.status = Status.IDLE
                else: self.status = Status.UP
        print(self.elevatorStatusDescription())
    
    def elevatorStatusDescription(self):
        text = (
            f"Status: {self.status}\n"
            f"Lvl: {self.now_lvl}\n"
            f"upStops: {self.upStops[1:]}\n"
            f"downStops: {self.downStops[1:]}\n"
        )
        return text
    
obj = Elevator(5)
obj.handleExternal(ExternalRequest(3, Status.DOWN))
obj.openGate()
obj.handleInternal(InternalRequest(1)) 
obj.closeGate()
obj.openGate()