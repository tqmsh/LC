class Solution:
    def _dfs(self, vis: set[str], ans: list[str], prev: str, n: int, k: int):
        # 两种：def _dfs(now), dfs(nxt), 
        #   即进 def _dfs(now) 门时, now 一切信息全部订好了，可以直接 vis[now] = 1, dfs(nxt)

        #   def _dfs(prev), dfs(now)
        #   即进 def _dfs(prev) 门时，prev 一切信息全部订好了, now 还得决定，决定好后 vis[now] = 1, dfs(𝜟now)

        # 进门前判断：
        #   即进 def _dfs(now) 门前, 在  dfs(nxt) 步时，用 now <-> nxt 做了事情，这样就不用进def _dfs(now) 之后判断了
        #   i.e. e[nxt].append(now)// if u.l and not u.r, return 

        # 进门后判断：
        #   即进 def _dfs(now) 门后，才对 now 的信息做操作
        #   i.e.  def _dfs(now); if not now: return;  vis[now] = 1; 
        
        # 这里用的是： def _dfs(prev), dfs(now)， 进门前判断
        
        for dx in range(k):
            now = prev + str(dx)
            if now not in vis:
                vis.add(now)
                self._dfs(vis, ans, now[1:], n, k)  
                ans.append(str(dx))  

    def crackSafe(self, n: int, k: int) -> str:
        prev = "0" * (n - 1)
        vis: set[str] = set()
        ans: list[str] = []   
        self._dfs(vis, ans, prev, n, k) 
        return "".join(ans) + prev # dfs 反的，所以得尾部加上 reverse(prev), 即 0000

print(Solution().crackSafe(2, 2))
