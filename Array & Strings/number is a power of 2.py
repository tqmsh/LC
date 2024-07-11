from math import log2
class Solution: 
    def check1(self, x):
        return x > 0 and log2(x).is_integer()
    def check2(self, x):
        return x > 0 and bin(x).count('1') == 1
    def solve(self, a):
        return [1 if self.check1(x) and self.check2(x) else 0 for x in a]
def main():
    solution = Solution()
    a = [1,2,3,4,5,16]
    out = solution.solve(a)
    print(out) 

if __name__ == "__main__":
    main()