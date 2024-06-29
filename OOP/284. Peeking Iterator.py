
class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator  # 走动器

        # cant do nxt(self.iter) coz we didnt make a iterator unlike the BT example
        self.ptr = self.iter.next() if self.iter.hasNext() else None    # 初始化指针至数列第一位

    def peek(self):
        return self.ptr  # 啥都不做

    def next(self):
        ans = self.ptr 
        self.ptr = self.iter.next() if self.iter.hasNext() else None
        return ans 

    def hasNext(self):
        return self.ptr is not None  # if node: f(node.left/right) 同理
 
# Usage example:
iter = PeekingIterator(iter([1, 2, 3])) 

print(iter.peek())  # Output: 1
print(iter.next())  # Output: 1
print(iter.peek())  # Output: 2
print(iter.next())  # Output: 2
print(iter.hasNext())  # Output: True
print(iter.next())  # Output: 3
print(iter.hasNext())  # Output: False
