


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
parent-child 노드끼리 계산만 가능하다
"""    
    # def isValidBST(self, root):

    #     result = []

    #     def dfs(root):
    #         nonlocal result

    #         if root is None:
    #             return

    #         if root.left is not None:
    #             if root.left.val >= root.val:
    #                 result.append(False)

    #             dfs(root.left)
                

    #         if root.right is not None:
    #             if root.right.val <= root.val:
    #                 result.append(False)

    #             dfs(root.right)
        
    #     dfs(root)

    #     if result == []:
    #         return True

    #     return False

