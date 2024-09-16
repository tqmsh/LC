from typing import List
 
def read4(buf4: List[str]) -> int: 
    file_content = "abcde" 
    if not hasattr(read4, "file_pointer"):
        read4.file_pointer = 0
    
    
    chars_read = 0
    while chars_read < 4 and read4.file_pointer < len(file_content):
        buf4[chars_read] = file_content[read4.file_pointer]
        read4.file_pointer += 1
        chars_read += 1
    
    return chars_read

class Solution:
    def __init__(self):
        self.now = [0] * 4 
        self.sz = self.ptr = 0

    def read(self, ans: List[str], n: int) -> int:
        # read4 可以给 buf4 送下 4 个物体，我们的任务是把它拿下
        i = 0
        while i < n:
            while i < n and self.ptr < self.sz: # 有的读，录
                ans[i] = self.now[self.ptr]
                self.ptr += 1; i += 1 
                
            self.sz = read4(self.now)
            if not self.sz: break # 没得读了
            self.ptr = 0
        return i
        

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    buf = [''] * 5
    num_chars = sol.read(buf, 4)  # Read up to 4 characters
    print(f"Read {num_chars} characters: {buf[:num_chars]}")  # Output should be ['a', 'b', 'c', 'd']
    
    buf = [''] * 5
    num_chars = sol.read(buf, 4)  # Try to read more characters
    print(f"Read {num_chars} characters: {buf[:num_chars]}")  # Output should be ['e']
    
    buf = [''] * 5
    num_chars = sol.read(buf, 1)  # Try to read more characters (should be 0)
    print(f"Read {num_chars} characters: {buf[:num_chars]}")  # Output should be []
