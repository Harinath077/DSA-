# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 ,t2 = l1, l2
        dummyNode = ListNode(None)
        curr = dummyNode
        carry = 0
        while t1 != None or t2 != None:
            sum_ = carry
            if t1 :
                sum_ = sum_ + t1.val
                t1 = t1.next
            if t2:
                sum_ = sum_ + t2.val
                t2 = t2.next
            newNode = ListNode(sum_ % 10)
            carry = sum_ // 10
            curr.next = newNode
            curr = curr.next
        if carry == 1:
            newNode = ListNode(1)
            curr.next = newNode
        return dummyNode.next

        