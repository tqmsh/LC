from typing import List, Optional

class NI:
    def __init__(self, value):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = value
    
    def isInteger(self) -> bool:
        return self._integer is not None
    
    def getInteger(self) -> int:
        if self.isInteger():
            return self._integer
        else:
            raise ValueError("This NI instance does not hold an integer.")
    
    def getList(self) -> List['NI']:
        if not self.isInteger():
            return self._list
        else:
            raise ValueError("This NI instance does not hold a list.")
        
class NestedIterator:
    def __init__(self, nestedList: List[NI]):
        self.flattened = self._flatten(nestedList)
        self.i = 0

    def _flatten(self, nested: List[NI]) -> List[int]:
        ans = []
        for ni in nested:
            if ni.isInteger(): ans.append(ni.getInteger()) 
            else: ans.extend(self._flatten(ni.getList())) 
        return ans

    def next(self) -> int: # 输出当下数字，把 i 移动至下一个轮回, i.e. for i in range(...): print(i)
        if not self.hasNext(): raise StopIteration("No more elements.")
        result = self.flattened[self.i]
        self.i += 1
        return result

    def hasNext(self) -> bool: # 当下数字 i 是否合法
        return self.i < len(self.flattened)

def test_iterator():
    # Create a nested structure: [1, [4, [6]], 2]
    nested_list = [
        NI([NI(1), NI(2)]),
        NI(3)
    ]
    
    iterator = NestedIterator(nested_list)
    
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    
    print(result)  # Expected output: [1, 2, 3]

test_iterator()