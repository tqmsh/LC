import re
from collections import Counter
class Solution: 
    def most_common_words(self, text):  
        text = text.lower()
        # Remove punctuation
        # re sub 模版
        text = re.sub(r'[^\w\s]', '', text)   
        words = text.split()
        word_counts = sorted(Counter(words).items(), key = lambda x: (-x[1], x[0])) # 按照 x[1] 从大到小
        # mp sort 模版
        return word_counts
def main():
    solution = Solution()  
    text = 'It was the best of times, it was the worst of times.' 
    out = solution.most_common_words(text)
    print(out) 

if __name__ == "__main__":
    main()