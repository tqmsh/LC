class Vector2D: 
    def __init__(self, a):
        self.i = 0
        self.a = [x for y in a for x in y]
    def next(self):
        num = self.a[self.i]
        self.i += 1
        return num
    def hasNext(self):
        return self.i <= len(self.a) - 1

 
operations = ["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
parameters = [[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]  
obj = None
for op, param in zip(operations, parameters):
    if op == "Vector2D":
        obj = Vector2D(*param) 
        print("null", end=" ")
    elif op == "next":
        print(obj.next(*param), end=" ") 
    elif op == "hasNext":
        print(obj.hasNext(*param), end=" ")  