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
    private ListNode getKNode(ListNode temp, int k){
        k--;
        while( temp != null && k > 0 ){
            temp = temp.next;
            k--;
        }
        return temp;
    }
    private ListNode reverse(ListNode head){
        ListNode prev = null;
        ListNode curr = head;
        while(curr != null){
            ListNode front = curr.next;
            // change the Link
            curr.next = prev;
            // move the pointers
            prev = curr;
            curr = front;
        }
        return prev;
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        if( head == null && head.next == null && k == 1){
            return head;
        }
        ListNode prevLast = null;
        ListNode temp = head;

        while( temp != null){
            // get Kth node
            ListNode kthNode = getKNode(temp, k);

            // edge case
            if( kthNode == null){
                if( prevLast != null){
                    prevLast.next = temp;
                }
                break;
            }

            ListNode nextNode = kthNode.next;
            // unLink
            kthNode.next = null;

            // reverse the k group LL
            ListNode newHead = reverse(temp);

            // edge case : first kth group ( for head )
            if( temp == head){
                head = newHead;
            }else{
                prevLast.next = newHead;
            }

            prevLast = temp;
            temp = nextNode;
        }
        return head;

    }
}