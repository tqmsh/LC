from bisect import bisect_left
class LineNumberFinder():
    def __init__(self, file: str):
        self.a = [i for i, char in enumerate(file) if char == '\n']  
    def find(self, offset: int):
        return bisect_left(self.a, offset) + 1
    
    
file_content = "abc\nde\nefg\nh\n"
finder = LineNumberFinder(file_content)
print(finder.find(7))  # Expected output: 2