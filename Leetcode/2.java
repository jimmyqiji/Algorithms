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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }
        int digitSum = l1.val + l2.val;
        int carryover = digitSum / 10;
        if (digitSum < 10 && l1.next == null && l2.next == null) {
            return new ListNode(digitSum);
        }
        return new ListNode(digitSum % 10, addTwoNumbers(l1.next, addTwoNumbers(l2.next, new ListNode(carryover, null))));
    }
}