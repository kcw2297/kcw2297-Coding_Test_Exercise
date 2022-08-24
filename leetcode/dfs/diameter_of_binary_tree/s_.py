# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        if root is None: return 0
    
        result = 0
        
        def dfs(root):
            if root is None: return 0
            nonlocal result
            
            rightMax = dfs(root.right)
            leftMax = dfs(root.left)
            
            curMax = rightMax + leftMax
            result = max(result, curMax)
            return 1 + max(rightMax, leftMax)
        
        dfs(root)
        return result

"""
하나의 함수안에 2가지의 기능이 존재 

1. result에 최대 값을 계산해서 전달하는 기능
2. 다음 재귀함수에 값을 전달하는 기능

문제 풀이시 아래와 같이 나누어서 생각을 한다
"""


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        if root is None: return 0
    
        result = 0
        
        def dfs(root):
            if root is None: return 0
            nonlocal result
            
            rightMax = dfs(root.right)
            leftMax = dfs(root.left)
            curMax = rightMax + leftMax
            
            newResult(curMax)
            return 1 + max(rightMax, leftMax)
        
        def newResult(max):
            nonlocal result
            if max > result:
                result = max
        
        dfs(root)
        return result
            