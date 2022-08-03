class Solution:
    def missingNumber(self, nums):
        
        tot = len(nums)
        tot_range = [i for i in range(tot+1)]


        return [i for i in tot_range if i not in nums][0]