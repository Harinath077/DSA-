# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findNode(temp,k):
            count = 1
            while(temp != None):
                if count == k:
                    return temp
                count += 1
                temp = temp.next
            return temp
        
        if head == None or k == 0:
            return head
        length = 1
        tail = head
        while(tail.next != None):
            length += 1
            tail = tail.next
        if k % length == 0:
            return head
        k = k % length
        tail.next = head
        newLast = findNode(head,length-k)
        head = newLast.next
        newLast.next = None
        return head

                
            
            
        