#https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        return self.quickSelect(nums,0,len(nums)-1,k)

    def quickSelect(self, nums, lo, hi, k):
        pivot = nums[hi]
        i = lo

        for j in range(lo,hi):
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1
        
        self.swap(nums, hi, i)

        if i > k:
            return self.quickSelect(nums, lo, i-1, k)

        elif i < k:
            return self.quickSelect(nums, i+1, hi, k)
        else:
            return nums[i]


    def swap(self, nums, idx1, idx2):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp
        return
