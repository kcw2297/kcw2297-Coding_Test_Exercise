# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums):
        if len(nums) == 1: return nums

        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        self.sortArray(left)
        self.sortArray(right)

        i = j = k = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        
        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1


        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1


        return nums

