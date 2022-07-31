
        
"""
This is the approach passing through the root
failed, because some path may not pass through the root

root를 기준으로 생각을 한 케이스이지만, 반대로 leaf를 기준으로 생각시에
최대 변의 길이의 중심 점이 달라질 수 있다.
"""
        
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        def dfs(root, h):
            if root is None:
                return h - 1
            
            return max(dfs(root.right, h+1), dfs(root.left, h+1), 0)
        
        
        return max(dfs(root.left, 1) + dfs(root.right,1))
        