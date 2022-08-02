


class Solution:

    def __init__(self):
        self.flag = True
        self.curr = float("-inf")
        
    
    def isValidBST(self, root):
        if root is None:
            return

        self.isValidBST(root.left)

        if root.val <= self.curr:
            self.flag = False

        self.curr = root.val

        self.isValidBST(root.right)

        return self.flag

"""
inorder, preorder, postorder을 이용해 순회하는 방법을 고려하자
"""