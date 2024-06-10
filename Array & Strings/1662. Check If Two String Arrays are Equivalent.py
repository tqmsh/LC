class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # .join 模版
        if ''.join(word1) == ''.join(word2):
            return True
        return False