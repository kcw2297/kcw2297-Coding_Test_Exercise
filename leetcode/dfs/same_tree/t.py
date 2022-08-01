class Solution:
    def isSameTree(self, p, q):
        
        a = []     
        b = []
        
        def dfs(root, container):
            nonlocal a
            nonlocal b
            
            
            if root is None:
                return 
            if container == a:
                a.append(root.val)
            else:
                b.append(root.val)
            dfs(root.left, container)
            dfs(root.right, container)

        dfs(q,b)
        dfs(p,a)
        
        return a == b

"""
2개의 트리를 dps를 통해 container안에 저장한 후 값을 비교한다
"""


