def inorderTraversal(self, root):
        
        output=[]
        def inorder(root):
            nonlocal output
            if not root:
                return [] # If no root then return empty list
            
            if root.left:
                inorder(root.left) # Check the left side
            
            output.append(root.val) # Take the value of the current node (root)
            
            if root.right:
                inorder(root.right) # Check the right side
        
        inorder(root)
        return output