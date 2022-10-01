class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid])

        root.left = self.helper(nums, left, mid-1)

        root.right = self.helper(nums, mid+1, right)

        return root