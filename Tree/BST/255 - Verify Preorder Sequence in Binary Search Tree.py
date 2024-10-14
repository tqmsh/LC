class Solution:
    def verifyPreorder(self, preorder): 
        stk = []
        now_rt = -float('inf')

        # pre 转 in 模版
        for x in preorder:
            # now_rt: 当下母节点，现在处理的是 now_rt 的右边子树
            if x < now_rt: return 0  
            while stk and x > stk[-1]: now_rt = stk.pop() # 更新 now_rt
            stk.append(x)
        return 1
    def constant_space(self, preorder):
        now_rt = -float('inf')
        j = -1 # stk idx
        for x in preorder: # [0, x) 都用不着了，每次 i += 1, j 顶多 += 1, 无法和 i 产生冲突
            if x < now_rt: return 0
            while j >= 0 and x > preorder[j]: 
                now_rt = preorder[j] # now_rt = stk[-1]
                j -= 1 # stk.pop()
            j += 1
            preorder[j] = x
        return 1
print(Solution().constant_space([5,2,1,3,2.5,6]))