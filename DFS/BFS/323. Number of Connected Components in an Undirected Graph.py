from typing import List  

class Solution:
    def _find(self, x, f):
        if f[x] == x: return x 
        f[x] = self._find(f[x], f) 
        return f[x]
    
    def _merge(self, x, y, f): # 把 x 添到 y 下
        Fx = self._find(x, f)
        Fy = self._find(y, f)
        if Fx != Fy: f[Fx] = Fy 

    def countComponents(self, n: int, edges: List[List[int]]) -> int:  
        # 并查集 模版
        f = list(range(n))
        for u, v in edges: self._merge(u, v, f) 
        return sum(i == self._find(i, f) for i in range(n)) 
    
def main(): 
    solution = Solution() 
    assert solution.countComponents(1, []) == 1

    # Test case 2: Two nodes, no edges
    assert solution.countComponents(2, []) == 2

    # Test case 3: Two nodes, one edge
    assert solution.countComponents(2, [[0, 1]]) == 1

    # Test case 4: Three nodes, two connected
    assert solution.countComponents(3, [[0, 1]]) == 2

    # Test case 5: Three nodes, fully connected
    assert solution.countComponents(3, [[0, 1], [1, 2]]) == 1

    # Test case 6: Four nodes, two separate components
    assert solution.countComponents(4, [[0, 1], [2, 3]]) == 2

    # Test case 7: Four nodes, all connected in a cycle
    assert solution.countComponents(4, [[0, 1], [1, 2], [2, 3], [3, 0]]) == 1

    # Test case 8: Five nodes, three components
    assert solution.countComponents(5, [[0, 1], [2, 3]]) == 3

    # Test case 9: Nodes in a star configuration
    assert solution.countComponents(5, [[0, 1], [0, 2], [0, 3], [0, 4]]) == 1

    # Test case 10: Disconnected graph
    assert solution.countComponents(6, [[0, 1], [2, 3], [4, 5]]) == 3

    print("All test cases pass")

if __name__ == "__main__":
    main()