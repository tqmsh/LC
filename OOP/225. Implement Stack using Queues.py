from collections import deque
class MyStack: 
    # queue 模版
    def __init__(self):  
        self.q = deque() 
    def push(self, x: int) -> None: 
        self.q.append(x)
        for i in range(len(self.q) - 1): self.q.append(self.q.popleft())  
    def pop(self) -> int:
        return self.q.popleft()
    def top(self) -> int: 
        return self.q[0]
    def empty(self) -> bool:
        return len(self.q) == 0 

# Usage example: 

operations = ["MyStack", "push", "push", "top", "pop", "empty"]
parameters = [[], [1], [2], [], [], []]

obj = None
for op, param in zip(operations, parameters):
    if op == "MyStack":
        obj = MyStack(*param)
        print("null", end=" ")
    elif op == "push":
        obj.push(*param)
        print("null", end=" ")
    elif op == "pop":
        result = obj.pop(*param)
        print(result, end=" ")
    elif op == "top":
        result = obj.top(*param)
        print(result, end=" ")
    elif op == "empty":
        result = obj.empty(*param)
        print(result, end=" ")