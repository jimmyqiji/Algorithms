# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minpq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(minpq, [lists[i].val, i, lists[i]])
                lists[i] = lists[i].next
        start = None
        prev = None
        while len(minpq) > 0:
            [_, list_i, item] = heappop(minpq)
            if not start:
                start = item
            if prev:
                prev.next = item
            prev = item
            if lists[list_i]:
                heappush(minpq, [lists[list_i].val, list_i, lists[list_i]])
                lists[list_i] = lists[list_i].next
        return start