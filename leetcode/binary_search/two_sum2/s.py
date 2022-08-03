"""
binary search는 정렬된 리스트 안의 조합을 찾을 시 유용하다.
지속적으로 절반으로 나누어 계산하는 식 존재.
"""


class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while True:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            
            if numbers[left] + numbers[right] > target:
                right -= 1
            
            if numbers[left] + numbers[right] < target:
                left += 1
            
            if left >= right:
                return False