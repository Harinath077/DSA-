/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // base cases
        if( list1 == null && list2 != null ) return list2;
        if( list2 == null && list1 != null ) return list1;

        ListNode dummy = new ListNode(-1);
        ListNode curr = dummy;
        ListNode t1 = list1;
        ListNode t2 = list2;
        while( t1 != null && t2 != null){
            if( t1.val <= t2.val){
                curr.next = t1;
                t1 = t1.next;
            }
            else{
                curr.next = t2;
                t2 = t2.next;
            }
            curr = curr.next;
        }

        // edge cases
        if( t1 != null){
            curr.next = t1;
        }
        else{
            curr.next = t2;
        }
        return dummy.next;
    }
}