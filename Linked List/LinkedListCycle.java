/**
 * Definition for singly-linked list.
 * class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) {
 * val = x;
 * next = null;
 * }
 * }
 */
public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        ListNode slowPtr = head;
        ListNode fastPtr = head.next;
        int slowPos = 0;
        int fastPos = 1;

        while (fastPtr != null) {
            if (slowPtr == fastPtr) {
                return true;
            }

            if (slowPos % 2 == 0) {
                slowPtr = slowPtr.next;
            }
            fastPtr = fastPtr.next;
            slowPos++;
            fastPos++;
        }

        return false;
    }
}