class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Step 1: In-order traversal to collect sorted values
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: Build a balanced BST from sorted values
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(vals[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node

        return build(0, len(vals) - 1)
