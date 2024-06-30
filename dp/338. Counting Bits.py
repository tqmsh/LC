from typing import List  
# decimal_to_binary 模版
def decimal_to_binary(n):
    if n == 0:
        return '0'
    
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    
    return binary

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)  
        for i in range(1, n + 1):  
            dp[i] = dp[i >> 1] + (i & 1) 
            #1, 0   #1            #0
            
        return dp 
    
def main():
    solution = Solution()  
    n = 2 
    out = solution.countBits(n)
    print(out) 

if __name__ == "__main__":
    main()
