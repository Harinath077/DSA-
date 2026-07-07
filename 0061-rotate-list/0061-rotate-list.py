# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        k = k%len(arr)
        arr = arr[-k:] + arr[:-k]
        temp = head
        i = 0
        while(temp != None):
            temp.val = arr[i]
            temp = temp.next
            i += 1
        return head

                
            
            
        