#https://leetcode.com/problems/sort-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head


        mid = self.divhalf(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)



    def divhalf(self, head):
        midPrev = None
        while head is not None and head.next is not None:
            if midPrev == None:
                midPrev = head
            else:
                midPrev = midPrev.next

            head = head.next.next

        mid = midPrev.next
        midPrev.next = None
        return mid

    def merge(self, left, right):
        dummyHead = ListNode()
        tail = dummyHead

        while left is not None and right is not None:
            if left.val < right.val:
                tail.next = left
                left = left.next
                tail = tail.next
            else:
                tail.next = right
                right = right.next
                tail = tail.next

        while left is not None:
            tail.next = left
            left = left.next
            tail = tail.next

        while right is not None:
            tail.next = right
            right = right.next
            tail = tail.next
        
        # if left != None:
        #     tail.next = left
        # else:
        #     tail.next = right



        return dummyHead.next
