from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans

def main():
    print(12)
    solution = Solution()
    
    words1 = ["leet", "code"]
    x1 = "e" 
    out = solution.findWordsContaining(words1, x1)
    print(out) 

if __name__ == "__main__":
    main()