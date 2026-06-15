# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ 
    find the length and change the links
    """
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if( head is None or head.next is None):
            return None
        
        # find the middle node
        temp = head
        length = 0
        while( temp != None):
            length += 1
            temp = temp.next
        mid = length // 2

        # delete the middle node / change the links
        curr = head
        while( curr != None ):
            mid -= 1
            if( mid == 0 ):
                curr.next = curr.next.next
            curr = curr.next
        return head
