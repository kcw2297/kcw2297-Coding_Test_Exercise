


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)

    if node.key == key:
        return "Cannot have duplicate number"

    if node.key < key:
        node.right = insert(node.right, key)
    if node.key > key:
        node.left = insert(node.left, key)

    return node

def minValueNode(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def deleteNode(root, key):
    
    # tree의 마지막 node에 도달(base case)
    if root is None:
        return root
    
    # 왼쪽 branch 조사
    if key < root.key:
        root.left = deleteNode(root.left, key)
    
    # 오른쪽 branch 조사
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    
    else:
        # 해당 root를 삭제해야하는 경우 및 자식 노드가 1개이거나 없는 경우
        if root.left is None:
            temp = root.right
            root = None
            return temp 
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        # 가장 최상단의 root가 삭제해야하는 경우
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root