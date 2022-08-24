from collections import deque

class Solution:

    def minDepth(self, root):
        if root is None: return 0

        result = 0

        container = deque()
        container.append(root)

        while container:
            
            result += 1

            for i in range(len(container)):
                temp = container.popleft()
                
                if not temp.left and not temp.right:
                    return result
                
                if temp.left:
                    container.append(temp.left)
                
                if temp.right:
                    container.append(temp.right)
            
        return result
