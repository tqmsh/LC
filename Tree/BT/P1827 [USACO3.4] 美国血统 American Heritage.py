def find_postorder(inorder, preorder): 
    idx = {val: idx for idx, val in enumerate(inorder)} 
    def dfs(in_left, in_right, pre_left, pre_right): 
        # inorder: 左根右
        # preorder: 根左右

        if in_left > in_right or pre_left > pre_right: return "" 

        # Root value from preorder
        root_val = preorder[pre_left]
        root_idx = idx[root_val]
        
        # Left and right subtree sizes
        left_tree_size = root_idx - in_left # [in_L, rt)
        
        # Recursive traversal for left and right subtrees and then the root (postorder)
        left_part = dfs(in_left, root_idx - 1, pre_left + 1, pre_left + left_tree_size)
        right_part = dfs(root_idx + 1, in_right, pre_left + left_tree_size + 1, pre_right)
        return left_part + right_part + root_val

    # Initial call
    return dfs(0, len(inorder) - 1, 0, len(preorder) - 1)

# Sample input
inorder = "ABEDFCHG"
preorder = "CBADEFGH"
print(find_postorder(inorder, preorder))  # Expected output: "AEFDBHGC"
