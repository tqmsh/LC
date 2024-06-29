
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}

    def get(self, key: int) -> int:
        if key not in self.mp: return -1
        self.mp[key] = self.mp.pop(key) # (k, v) 刚拿过，放堆顶， i.e. {..., (k, v)}
        return self.mp[key]

    def put(self, key: int, value: int) -> None:  
        if key in self.mp: self.mp.pop(key) # 必须放堆顶，更新地址
        else:
            if self.capacity: self.capacity -= 1   
            else: self.mp.pop(next(iter(self.mp))) # 移除一个（key, value）pair  
        self.mp[key] = value
# Usage example: 

operations = ["LRUCache","put","put","put","put","get","get"]
parameters = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

obj = None
for op, param in zip(operations, parameters):
    if op == "LRUCache":
        obj = LRUCache(*param)
        print("null", end=" ")
    elif op == "put":
        obj.put(*param)
        print("null", end=" ")
    elif op == "get":
        result = obj.get(*param)
        print(result, end=" ")