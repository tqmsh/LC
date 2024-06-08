import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False

# Trie 模版
class Trie:
    def __init__(self): 
        self.root = TrieNode() # 初始化Trie树的根节点

    def insert(self, path): 
        curr = self.root # 插入路径到Trie树中
       
        for i in range(len(path)):  # 遍历路径中的每个部分
            
            curr = curr.children[path[i]] # 移动到当前部分对应的子节点，如果不存在则创建
        
        curr.end = True # 标记路径的结束

    def search(self, path):
        
        curr = self.root # 搜索路径是否存在且不是其他路径的子文件夹
       
        for i in range(len(path)): # 遍历路径中的每个部分
            
            curr = curr.children[path[i]] # 移动到当前部分对应的子节点
            
            if curr.end and i != len(path) - 1: # 如果当前节点是一个结束节点且不是路径的最后一个部分，则返回False
                return False
            
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        ans = []

        for x in folder:
            # split 模版
            trie.insert(x.split("/"))

        # 现在 trie 维持的是这样的 a (end) -> b (end)，所以如果找 a -> b, 会在 a 这里卡死
        for x in folder:
            if trie.search(x.split("/")): # 找到了完整的，即 
                ans.append(x)

        return ans

def main(): 
    solution = Solution() 
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"] 
    out = solution.removeSubfolders(folder) 
    print(out)

if __name__ == "__main__":
    main()
