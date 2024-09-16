from typing import List, Union

class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self._list = []
            self._integer = None
        elif isinstance(value, int):
            self._list = None
            self._integer = value
        elif isinstance(value, list):
            self._list = value
            self._integer = None
        else:
            raise ValueError("Invalid value type")

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        if self.isInteger():
            return self._integer
        else:
            return None

    def getList(self) -> List['NestedInteger']:
        if not self.isInteger():
            return self._list
        else:
            return None

    def add(self, ni: 'NestedInteger'):
        if not self.isInteger():
            self._list.append(ni)

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        q = nestedList
        sums = []
        while q:
            sum = 0
            for _ in range(len(q)): # 进门后处理，一般都是进门前处理，即 if in == 0 -> 进 q，
                                    # 但是这里这样难，还不如全部进来，然后做判断, i.e. 是否 in == 0
                now = q.pop(0)
                if now.isInteger(): sum += now.getInteger() # in = 0, ok
                else: q.extend(now.getList()) # propagate v = e[u], v in--, give to q, q will determine if next inn = 0
            sums.append(sum)
        ans = 0
        for i, sum in enumerate(sums): ans += (len(sums) - i) * sum
        return ans

# Example usage:
nestedList = [
    NestedInteger([NestedInteger(1), NestedInteger(1)]),
    NestedInteger(2),
    NestedInteger([NestedInteger(1), NestedInteger(1)])
]

sol = Solution()
print(sol.depthSumInverse(nestedList))  # Output should match the problem description
