from typing import List 
from collections import defaultdict
class Solution: 
    def getHint(self, secret: str, guess: str) -> str:
        secret_cnt = defaultdict(int)
        guess_cnt = defaultdict(int)
        num_bulls = 0; num_cows = 0
        # 边枚举边计算
        for i in range(len(secret)):
            if secret[i] == guess[i]: num_bulls += 1
            else:
                if guess_cnt[secret[i]] > 0: # 可以匹配
                    num_cows += 1
                    guess_cnt[secret[i]] -= 1 # 则匹配
                else: secret_cnt[secret[i]] += 1 # 否则存着，以后匹配

                if secret_cnt[guess[i]] > 0: # 可以匹配
                    num_cows += 1
                    secret_cnt[guess[i]] -= 1 # 则匹配
                else: guess_cnt[guess[i]] += 1 # 否则存着，以后匹配
        return str(num_bulls) + 'A' + str(num_cows) + 'B'
def main():
    solution = Solution()   
    secret = "1123"; guess = "0111"
    out = solution.getHint(secret, guess)
    print(out) 

if __name__ == "__main__":
    main()
