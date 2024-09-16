from typing import List
from collections import defaultdict, Counter
def word_count_engine(document: str) -> List[List[str]]:
    words = document.split(" ")
    processed_words = [] 
    idx = defaultdict(lambda: -1)
    for i in range(len(words)):
        
        word = words[i]
        word = word.lower() 
        ans = ""
        for j in range(len(word)): 
            if not (word[j] in ["?",",",".", "'", "!", ":", ";"]): ans += word[j]
        if ans is "": continue
        processed_words.append(ans)
        if idx[ans] == -1: idx[ans] = i
    cnt = Counter(processed_words)
    cnt = sorted(cnt.items(), key = lambda x: (-x[1], idx[x[0]]))
    ans = []
    for word, freq in cnt: ans.append([word, str(freq)])
    return ans
print(word_count_engine("Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"))


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