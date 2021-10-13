# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = left
        start = head
        right = right - left
        prevChunk = None
        while left > 1:
            prevChunk = head
            head = head.next
            left -= 1
            
        startOfChunk = head
        prev = None
        while right+1 > 0:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            right -= 1
        
        if prevChunk:
            prevChunk.next = prev
        if startOfChunk:
            startOfChunk.next = head
        if l == 1: 
            return prev 
        else:
            return start
