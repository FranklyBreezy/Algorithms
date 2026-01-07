# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxProduct(self, root):
        MOD = 10**9 + 7
        
        # Increase recursion limit for deep trees
        import sys
        sys.setrecursionlimit(10**7)
        
        # 1st pass: compute total sum
        def get_total_sum(node):
            if not node:
                return 0
            return node.val + get_total_sum(node.left) + get_total_sum(node.right)
        
        total_sum = get_total_sum(root)
        self.max_product = 0
        
        # 2nd pass: compute subtree sums and maximize product
        def dfs(node):
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            subtree_sum = node.val + left_sum + right_sum
            
            # Product if we cut above this subtree
            product = subtree_sum * (total_sum - subtree_sum)
            self.max_product = max(self.max_product, product)
            
            return subtree_sum
        
        dfs(root)
        return self.max_product % MOD
