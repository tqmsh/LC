class Count:
    def __init__(self, num = 0):
        self.ptr = num
    def __iter__(self):
        return self
    def __next__(self):
        num = self.ptr
        self.ptr += 1
        return num
class ArrayIterator:
    def __init__(self, arr):
        self.arr = arr
        self.ptr = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.ptr < len(self.arr):
            num = self.arr[self.ptr]
            self.ptr += 1
            return num
        else:
            raise StopIteration
    
counter = Count(1)
for _ in range(5):
    print(next(counter))
arrIterator = ArrayIterator([1,2,3,4,5])
for _ in range(5):
    try: print(next(arrIterator))
    except StopIteration: pass
