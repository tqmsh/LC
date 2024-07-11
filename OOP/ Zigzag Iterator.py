class ZigzagIterator: 
    q = []
    def __init__(self, a):
        for _, x in enumerate(a):
            self.q.append((0, x))
    def next(self):
        current_idx, current_arr = self.q.pop(0)
        next_idx = current_idx + 1  
        if next_idx < len(current_arr): self.q.append((next_idx, current_arr)) 
        return current_arr[current_idx]
    def hasNext(self):
        return len(self.q) != 0 
v1 = [1, 2]
v2 = [3, 4, 5, 6]
zigzag = ZigzagIterator([v1, v2])
result = []
while zigzag.hasNext():
    result.append(zigzag.next())
print(result)