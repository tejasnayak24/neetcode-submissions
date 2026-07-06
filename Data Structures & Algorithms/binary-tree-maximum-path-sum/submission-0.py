# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(root):
            nonlocal res
            if not root:
                return
            left = self.getMax(root.left)
            right = self.getMax(root.right)
            res =max(res, root.val + left + right)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    def getMax(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.getMax(root.left)
        right = self.getMax(root.right)
        path = root.val + max(left, right)
        return max(0, path)