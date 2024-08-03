from collections import defaultdict
class SparseVector:
    def __init__(self, sz):
        self.sz = sz
        self.mp = defaultdict(int)
    def set(self, idx, v): self.mp[idx] = v 
    def get(self, idx): return self.mp[idx]
    def __str__(self): return str(dict(self.mp))
vec = SparseVector(10)
vec.set(2, 3)
vec.set(5, 7)
vec.set(9, 1)
print(vec)  # Output: {2: 3, 5: 7, 9: 1}
