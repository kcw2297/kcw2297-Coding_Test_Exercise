class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        arr = []
        sentinel = ListNode(next = head)
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        c = 0 
        head2 = sentinel.next
        while head2:
            head2.val = arr[c]
            c += 1
            head2 = head2.next
        return sentinel.next

    

class Solution:
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def merge(list1, list2):
        dummyHead = ListNode()
        tail = dummyHead
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        
        if list1 != None:
            tail.next = list1
        else:
            tail.next = list2
        return dummyHead.next
            
            
    def getMid(head):
        midPrev = None
        while head != None and head.next != None:
            if midPrev == None:
                midPrev = head
            else:
                midPrev = midPrev.next
            
            head = head.next.next
        
        mid = midPrev.next
        midPrev.next = None
        return mid
            
            