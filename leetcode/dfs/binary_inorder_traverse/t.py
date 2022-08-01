"""
Input: root = [1,null,2,3]
Output: [1,3,2]
"""


class Solution:
    def inorderTraversal(self, root):

        if root is None:
            return []

        result = []

        def dfs(root):
            nonlocal result
            
            if root is None:
                return
            
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
            
        

        dfs(root)
        return result