# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None 
        walker = head
        runner = head
        while runner and runner.next:
            runner = runner.next.next
            tmp = walker.next
            walker.next = prev
            prev = walker
            walker = tmp
        if runner != None:
            walker = walker.next
        while prev and walker:
            if prev.val != walker.val:
                return False
            prev = prev.next
            walker = walker.next
        return prev == walker == None