
from collections import deque

class Solution:
    def isSymmetric(self, root):
        result = True

        container = deque()
        container.append(root)

        while container:
            temp_list = []

            for _ in range(len(container)):
                ele = container.popleft()
                temp_list.append(ele.val)

                
                if ele.left:
                    container.append(ele.left)

                if ele.right:
                    container.append(ele.right)

            if temp_list:
                half = len(temp_list)//2
                first = temp_list[0:half]
                second = temp_list[half:].reverse()
                if first != second:
                    return False

        return result
