import sys


N = int(sys.stdin.readline())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]


def preorder(tree, root):
    if root != '.':
        print(root, end = '')
        preorder(tree, tree[root][0])
        preorder(tree, tree[root][1])
    return


def inorder(tree, root):
    if root != '.':
        inorder(tree, tree[root][0])
        print(root, end = '')
        inorder(tree, tree[root][1])
    return


def postorder(tree, root):
    if root != '.':
        postorder(tree, tree[root][0])
        postorder(tree, tree[root][1])
        print(root, end = '')
    return

preorder(tree,'A')
print()
inorder(tree,'A')
print()
postorder(tree,'A')


# count = int(sys.stdin.readline())
# tree_list = list(sys.stdin.readline().split())

# for _ in range(count-1):
#     node_list = list(sys.stdin.readline().split())
#     root, left, right = node_list
#     tree_list.append(left)
#     tree_list.append(right)

# def preorder(tree_list,n):
#     if tree_list[n] != '.':
#         print(tree_list[n], end='')
#         preorder(tree_list,n*2+1)
#         preorder(tree_list,n*2+2)
#     return

# def inorder(tree_list,n):
#     if tree_list[n] != '.':
#         inorder(tree_list,n*2+1)
#         print(tree_list[n], end='')
#         inorder(tree_list,n*2+2)
#     return

# def postorder(tree_list,n):
#     if tree_list[n] != '.':
#         postorder(tree_list,n*2+1)
#         postorder(tree_list,n*2+2)
#         print(tree_list[n], end='')
#     return

# preorder(tree_list, 0)
# print()
# inorder(tree_list, 0)
# print()
# postorder(tree_list, 0)
