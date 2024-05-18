class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        # set 模版
        return len(set(sentence)) == 26