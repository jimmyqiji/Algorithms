from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = deque()
        start = 0
        end = len(nums)-1
        while start <= end:
            a = nums[start] ** 2
            b = nums[end] ** 2
            if a > b:
                result.appendleft(a)
                start += 1
            else:
                result.appendleft(b)
                end -= 1
        return result