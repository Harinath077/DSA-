# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLL(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # Attach the remaining part
        curr.next = list1 if list1 else list2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = lists[0]
        for i in range(1, len(lists)):
            head = self.mergeLL(head, lists[i])

        return head