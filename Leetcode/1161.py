# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = Queue()
        q.put(root)
        q.put(None)
        max_sum_level = 0
        max_sum = -math.inf
        cur_sum = 0
        cur_level = 0
        while not q.empty():
            cur = q.get()
            if cur == None:
                cur_level += 1
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    max_sum_level = cur_level 
                cur_sum = 0
                if not q.empty():
                    q.put(cur)
                continue
            cur_sum += cur.val
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)
        return max_sum_level