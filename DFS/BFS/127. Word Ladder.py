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
    
    def _get_nxt(self, word, wordList):
        res = set()
        for ind in range(len(word)):
            for c in ascii_lowercase:
                cur = word[:ind] + c + word[ind + 1:]
                if cur in wordList: # _check
                    res.add(cur)
        return res

    def _bfs(self, beginWord, endWord, wordList, e): # 🟥 DFS 大致有两种。(1) 填坑，step = 当前填哪一个坑，path = [1, step) 的结果。
                                                     #                  (2) 走图, x = 现在在哪个坐标，path = [0, x) 的拐弯情况，就是走到 x, 用的路径, i.e. nx, path + 'R', R 为 x -> nx
        lvl = {beginWord} # q.push(s)
        wordList = set(wordList) # vis[s] = 1
        wordList -= lvl
        while lvl: # 一层之间不存在没有走过的check
            nxt_lvl = set()
            for now in lvl: # now = q.pop(0)
                for nxt in self._get_nxt(now, wordList):
                    nxt_lvl.add(nxt)
                    e[nxt].append(now)
            if endWord in nxt_lvl: # now == end, 因为是进门前对nxt 判断的，end in nxt 一次性把 nxt 全查一遍 (咱不能投方便进门后查，因为 e[v].add(u))
                break
            lvl = nxt_lvl # q.append(nxt)
            wordList -= nxt_lvl 
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        e = defaultdict(list)
        # (1) 用BFS构图
        # (2) 用DFS走图
        self._bfs(beginWord, endWord, wordList, e)
        return self._dfs(endWord, beginWord, e) 
    
def main(): 
    solution = Solution() 
    beginWord = "red"; endWord = "tax"; wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    out = solution.findLadders(beginWord, endWord, wordList) 
    print(out) 

if __name__ == "__main__":
    main()