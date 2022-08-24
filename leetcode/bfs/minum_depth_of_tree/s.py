from collections import deque

class Solution:

    def minDepth(self, root):
        minDepth  =  0
        if not root:
            return minDepth
        q = deque()
        q.append(root)
        while(q):
            sz = len(q)
            minDepth += 1
            for i in range(sz):
                temp = q.popleft()
                if(not temp.left and not temp.right):
                    return minDepth
                if(temp.left):
                    q.append(temp.left)

                if(temp.right):
                    q.append(temp.right)

        return minDepth
