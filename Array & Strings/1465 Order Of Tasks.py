from typing import List
class Node:
    def __init__(self, id, t, p): self.id = id; self.t = t; self.p = p
    def __lt__(self, other: 'Node'):
        if abs(self.p * other.t - other.p * self.t) <  1e-5: return self.id < other.id
        return self.p * other.t > other.p * self.t
class Solution:
    def getOrder(self, n, t, p):
        a: List[Node] = [Node(i + 1, t[i], p[i]) for i in range(n)]
        a = sorted(a)
        return ([x.id for x in a])
    