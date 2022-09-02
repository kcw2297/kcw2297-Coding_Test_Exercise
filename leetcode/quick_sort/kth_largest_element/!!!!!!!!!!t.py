#https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums, k):
        sorted = self.quicksort(nums)
        return sorted[len(nums)-k]
    
    def quicksort(self, nums):
        if len(nums) == 1 or nums == None: return

        if len(nums) == 2:
            if nums[0] > nums[1]:
                temp = nums[0]
                nums[0] = nums[1]
                nums[1] = temp
            return 

        pivot = len(nums) - 1

        lm = 0
        prevm = len(nums)-2

        while lm < prevm:
            if nums[lm] > nums[pivot]:
                temp = nums[lm]
                nums[lm] = nums[prevm]
                nums[prevm] = nums[pivot]
                nums[pivot] = temp
        
                lm += 1
                pivot -= 1
                prevm -= 1
        
        if nums[pivot] < nums[prevm]:
            temp  = nums[pivot]
            nums[pivot] = nums[prevm]
            nums[prevm] = temp

            pivot -= 1
        
        left = nums[:pivot]
        right = nums[pivot:]

        self.quicksort(left)
        self.quicksort(right)
        return nums


