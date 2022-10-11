# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        max_v = 0

        def dfs(root, c):
            nonlocal max_v
            if root is None:
                max_v = max(max_v, c)
                return  c
            count = 0
            
            dfs(root.left, c+1)
            dfs(root.right, c+1)
            return

        dfs(root,0)

        return max_v