from typing import List

class Solution: 
    def _get_lps(self, s):
        lps = [0] * len(s); l = 0; i = 1 
        while i < len(s):
            if s[i] == s[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0: l = lps[l - 1] 
                else:
                    lps[i] = 0
                    i += 1 
        return lps
        
    def numOfGeneOccurrences(self, dna, gene):
        lps = self._get_lps(gene)
        i = 0; j = 0; ans = 0
        while i < len(dna): 
            # 配对
            if dna[i] == gene[j]: 
                i += 1
                j += 1
            # 断开情况（1）
            if j == len(gene):
                ans += 1
                j = lps[j - 1] # 例如 dna = ...[ab]cd[ab]...
                                    # gene  = [ab]cd[ab]
                                    #             v   j, v = lps[j - 1]
                                    #  找到之后，下一个可以从 gene  = ab(c)dab 开始找，因为 ab 必然已经配对完成
            # 断开情况（2）
            elif i < len(dna) and dna[i] != gene[j]:
                if j != 0: j = lps[j - 1] # abcd[abX
                                          # [abcdab，让 x 在 c 这里继续尝试，拼[...
                else: i += 1
        return ans 
    
def main():
    solution = Solution()
    
    dnaSequence = "GTTTTAGAAAAG"; geneSequence = "TT" 
    out = solution.numOfGeneOccurrences(dnaSequence, geneSequence)
    print(out) 

if __name__ == "__main__":
    main()