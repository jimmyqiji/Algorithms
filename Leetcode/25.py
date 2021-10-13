# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        fast = head
        for i in range(k-1):
            fast = fast.next
        init = False
        start = None
        while fast:
            cur_k = k
            to_be_end = head
            prev = None
            while cur_k > 0:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
                
                cur_k -= 1
                if fast:
                    fast = fast.next
            if not init:
                init = True
                start = prev
            if fast:
                to_be_end.next = fast
            else:
                to_be_end.next = head
        return start