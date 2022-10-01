#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        #재귀함수와 bst 이론을 배합한 helper function사용
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, left, right):
        """
            노드 객체를 생성 후 root를 기준으로 left, right에 붙인다
        """
        if left > right:
            return None

        # 배열에 가운데 부분이 중심을 가진다
        mid = (left + right)//2
        root = TreeNode(val=nums[mid])

        #root를 기준으로 재귀적으로 left, right을 붙인다
        root.left = self.helper(nums,left, mid-1)
        root.right = self.helper(nums,mid+1, right)

        return root


