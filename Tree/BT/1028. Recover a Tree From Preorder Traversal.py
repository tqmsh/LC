from typing import List 
from typing import Optional 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:  
        ans = TreeNode(); 
        tmp = ans 
        lstDep = -1
        j = 0
        stk = []
        def getNxt(traversal, id): 
            dep = 0; str = ""; idd = 0
            for i in range (id, len(traversal)):
                x = traversal[i]
                if x == '-': 
                    if str == "": dep += 1
                    else:
                        idd = i
                        break 
                else:
                    str += x 
                    if i == len(traversal) - 1:
                        idd = i + 1 
            return dep, str, idd 
          
        def isok(j, lstDep):  
            cnt, ch, id = getNxt(traversal, j)
            if cnt == lstDep + 1: return 1
            else: return 0

        while j < len(traversal) and (stk or isok(j, lstDep)):
            # 模拟移至左边最深 （j 不合法就是坐到头了）
            while j < len(traversal) and isok(j, lstDep):  
                store = j
                dep, ch, j = getNxt(traversal, j)
                tmp.left = TreeNode(int(ch))
                stk += [(tmp.left, store, dep)]

                tmp = tmp.left; lstDep = dep   

            # 模拟左边到底了，往上倒滑至第一个有右岔路的地方，把 tmp ^ lstdep 维持到那个位置 
            if j < len(traversal):
                tmp, tmpID, tmpDep = stk.pop()  
                rDep, rCh, rj = getNxt(traversal, j)
                while tmpDep != rDep - 1:
                    tmp, tmpID, tmpDep = stk.pop()

                # 尝试去右边岔路，如果存在的话，下次就去 while tmp 移至左边最深了
                tmp.right = TreeNode(int(rCh))
                stk += [(tmp.right, j, rDep)]
                tmp = tmp.right
                lstDep = rDep  
                j = rj  
        return ans.left

def print_bst(node, level=0, label='.'):
    indent = '   ' * level
    if node is not None:
        print(f"{indent}-{label}: {node.val}")
        print_bst(node.left, level + 1, 'L')
        print_bst(node.right, level + 1, 'R')
    else:
        print(f"{indent}-{label}: None")
def main():
    solution = Solution() 
    out = solution.recoverFromPreorder("1-2--3---4---5--6---7") 
    print_bst(out)

if __name__ == "__main__":
    main()


# class Solution:
#     def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
#         stack = []
#         i = 0

#         while i < len(traversal):
#             # calculate the depth
#             depth = 0
#             while traversal[i] == '-':
#                 depth += 1
#                 i += 1

#             # calculate the value
#             value = ''
#             while i < len(traversal) and traversal[i] != '-':
#                 value += traversal[i]
#                 i += 1
#             value = int(value)

#             # create the node
#             curr_node = TreeNode(val = value)
            
#             # move to curr_level
#             while stack and len(stack) > depth:
#                 stack.pop()

#             # add
#             if stack:
#                 # left child
#                 if stack[-1].left is None:
#                     stack[-1].left = curr_node
#                 # right child
#                 else:
#                     stack[-1].right = curr_node
            
#             stack.append(curr_node)
#         return stack[0]