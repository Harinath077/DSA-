# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = l1
        arr1 = []
        while(temp != None):
            arr1.append(temp.val)
            temp = temp.next
        temp = l2
        arr2 = []
        while(temp != None):
            arr2.append(temp.val)
            temp = temp.next
            
        n1 = int("".join(map(str,arr1[::-1])))
        n2 = int("".join(map(str,arr2[::-1])))
        # sum 
        sum_ = list(map(int,str(n1+n2)))
        sum_.reverse()
        # Create a new linked list from the sum
        head = ListNode(sum_[0])
        temp = head
        for i in range(1, len(sum_)):
            temp.next = ListNode(sum_[i])
            temp = temp.next

        return head


        