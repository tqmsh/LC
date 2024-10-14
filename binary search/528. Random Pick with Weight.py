from bisect import bisect_left
from random import randint
from itertools import accumulate
from typing import List
class Solution: 
    def __init__(self, w: List[int]):
        self.a: List[int] = list(accumulate(w)) 
    def pickIndex(self) -> int: 
        return bisect_left(self.a, randint(1, self.a[-1]))
