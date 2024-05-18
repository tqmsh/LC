from typing import List

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # .find 模版
        x = word.find(ch)   
        a1 = list(word[:x + 1])
        # .reverse 模版
        a1.reverse()
        a2 = list(word[x + 1:])
        return "".join(a1 + a2)
 

def main(): 
    solution = Solution()
    word = "abcdefd"
    ch = "d"  
    out = solution.reversePrefix(word, ch)
    print(out) 

if __name__ == "__main__":
    main()