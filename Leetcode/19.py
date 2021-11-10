# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        runner = head
        for _ in range(n):
            runner = runner.next
        walker = head
        prev = None
        while runner != None:
            prev = walker
            walker = walker.next
            runner = runner.next
        if prev == None:
            return walker.next
        prev.next = walker.next
        return head