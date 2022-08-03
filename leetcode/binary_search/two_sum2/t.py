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



"""
[-3,3]이고 target이 0이면 에러 발생 
"""

class Solution:
    def twoSum(self, numbers, target):
        
        nums, check = self.checkNums(numbers, target)
        if check:
            first = numbers.index(nums[0])
            return [first + 1, numbers.index(nums[1], first+1) + 1]
        return [numbers.index(nums[0]) + 1, numbers.index(nums[1], ) + 1]
        
    def checkNums(self, container, target):
        for num in container:
            if num < 0 and (target+num) in container:
                return [num, (target+num)], False

            if num == target and container.count(num) >=2:
                return [num, num], True

            if (target-num) in container:
                return [num, (target-num)], False

"""
주어진 numbers가 양수일때만 가능하다
"""

# class Solution:
#     def twoSum(self, numbers, target):
        
#         container = self.checkContainer(numbers, target)
#         nums = self.checkNums(container, target)

#         return [container.index(nums[0]) + 1, container.index(nums[1]) + 1]
        
        

#     def checkContainer(self, numbers, target):
#         result = [] 
#         for i in numbers:
#             if target > i:
#                 result.append(i)
#             if target <= i:
#                 break
#         return result

#     def checkNums(self, container, target):
#         for num in container:
#             if num < 0 and (target+num) in container:
#                 return [num, (target+num)]
#             if (target-num) in container:
#                 return [num, (target-num)]

