#https://leetcode.com/problems/sort-an-array/

"""
배열을 매개변수로 주어지면, 참조형이 됨으로 이를 이용해 진행
분할 후 정복과정에서 핵심은 분할 후  정렬된 배열끼리 합치는 과정이다
이미 정렬된 부분 배열을 합치는 것은 쉽다
"""

class Solution:
    def sortArray(self, nums):
        if len(nums) == 1: return 


        mid = len(nums)//2
        L = nums[:mid]
        R = nums[mid:]

        self.sortArray(L)
        self.sortArray(R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
            
        return nums
