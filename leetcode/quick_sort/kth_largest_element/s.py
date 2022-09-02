
class Solution:
    def quickSelect(self, nums, lo, hi, k):
        pivot = nums[hi]
        p = lo

        for i in range(lo,hi):
            if nums[i]< pivot:
                self.swap(nums, i, p)
                p += 1

        self.swap(nums, hi, p)

        if p > k:
            return self.quickSelect(nums, lo, p-1, k)
        elif p < k:
            return self.quickSelect(nums, p+1, hi, k)
        else:
            return pivot

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        return

    #selection sort
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        return self.quickSelect(nums, 0, len(nums)-1, k)

