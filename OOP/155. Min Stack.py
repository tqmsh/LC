class MinStack: 
    def __init__(self):
        self.stk = []  # 后进先出，最后的即为最新的
    def push(self, val: int) -> None: 
        mn = self.getMin()
        if mn is not None: self.stk.append([val, min(mn, val)]) # 不能用 +=, 不然会被认为是俩单独的 arr ele，concat
        else: self.stk.append([val, val]) 
    def pop(self) -> None: 
        if self.stk: self.stk.pop()   
    def top(self) -> int: 
        return self.stk[-1][0] if self.stk else None
    def getMin(self) -> int: 
        return self.stk[-1][1] if self.stk else None
         

operations = ["MinStack","push","push","push","getMin","pop","top","getMin"]
parameters = [[],[-2],[0],[-3],[],[],[],[]]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2

# Additional test cases
minStack.push(-5)
minStack.push(2)
minStack.push(10)
print(minStack.getMin())  # Output: -5
minStack.pop()
print(minStack.top())     # Output: 2
print(minStack.getMin())  # Output: -5

minStack.push(-1)
print(minStack.getMin())  # Output: -5
minStack.pop()
print(minStack.getMin())  # Output: -5
minStack.pop()
print(minStack.getMin())  # Output: -2
print(minStack.top())     # Output: None (stack is empty)
print(minStack.getMin())  # Output: None (stack is empty)