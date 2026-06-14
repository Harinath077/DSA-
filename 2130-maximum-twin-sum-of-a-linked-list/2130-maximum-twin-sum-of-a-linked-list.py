# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    ALGO:
    1. Find middle (slow/fast)
    2. Reverse second half
    3. Compare both halves

    """
    def reverseLL( self, head):
        temp = head
        prev = None
        if( head.next is not None):
            curr = head.next
        while( temp.next != None ):
            temp.next = prev
            prev = temp
            temp = curr
            curr = curr.next
        temp.next = prev
        return temp

    def findMiddle( self, head):
        slow = head
        fast = head.next
        while( fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow
        # firstHalf = slow
        # secondHalf = slow.next
        # return firstHalf, secondHalf

    def pairSum(self, head: Optional[ListNode]) -> int:
        if( head is None ):
            return None
        
        middleNode = self.findMiddle(head)
        secondHalve = middleNode.next
        middleNode.next = None
     
        # reverse 2nd havle
        secondHalve = self.reverseLL(secondHalve)
        
        temp1 = head
        temp2 = secondHalve
        maxSum = 0
        while( temp1 != None and temp2 != None ):
            currSum = temp1.val + temp2.val
            maxSum = max( maxSum, currSum)
            temp1 = temp1.next
            temp2 = temp2.next

        return maxSum
