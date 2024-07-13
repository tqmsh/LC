from collections import defaultdict
from string import ascii_lowercase
from typing import List

class Solution:
    def _dfs(self, u, beginWord, e): # e 存的是 begin <- c 最短路径经过谁
        if u == beginWord:
            return [[u]] 
        ans = []
        for v in e[u]:  
            for path in self._dfs(v, beginWord, e):  
                ans.append(path + [u])   
        return ans

    def _bfs(self, beginWord, endWord, wordList, e): # 🟥 DFS 大致有两种。(1) 填坑，step = 当前填哪一个坑，cur = [1, step) 的结果。(2) 走图, x = 现在在哪个坐标，e = [1, x], e = [1, x)
        found = 0
        q = [beginWord] 
        wordList = set(wordList)
        
        while q:
            lvl_vis = set()
            for _ in range(len(q)): # 同长路径入入同一坐标，结果可能不同 (如果都是最短),
                word = q.pop(0) 

                # 扩散
                for i in range(len(word)):
                    # ascii_lowercase 模版
                    for c in ascii_lowercase:
                        nxt_word = word[:i] + c + word[i + 1:];  
                        if nxt_word in wordList and nxt_word != word:
                            found |= (nxt_word == endWord) 

                            if nxt_word not in e[word]: e[nxt_word].append(word) # 同样的坐标不同路径都需要来，但是不用继续扩散

                            # 为啥不能 path? 因为当 a -> b -> c & d -> b -> c 时，虽然两条路都需要，但是算法不允许任意一层继续扩散同一个字，所以必须
                            # 勾画这个图，就是 a <- b，而且 d <- b，这样当我们找到 c 后(必然最短)，我们就可以沿着图往回找了
                                 
                            if nxt_word not in lvl_vis: # 但是不用都继续扩散（和回溯不同之处，回溯是全部继续扩散）
                                lvl_vis.add(nxt_word)
                                q.append(nxt_word) 
                            
            wordList -= lvl_vis # 不同长度的入同一坐标没有意义，因为这个坐标能否能到终点已经被研究了，而且必然比现在的快
        return found
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        e = defaultdict(list)
        # (1) 用BFS构图
        # (2) 用DFS走图
        if self._bfs(beginWord, endWord, wordList, e):
            return self._dfs(endWord, beginWord, e) 
    
def main(): 
    solution = Solution() 
    beginWord = "red"; endWord = "tax"; wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    out = solution.findLadders(beginWord, endWord, wordList) 
    print(out) 

if __name__ == "__main__":
    main()