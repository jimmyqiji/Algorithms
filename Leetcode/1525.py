class Solution:
    def numSplits(self, s: str) -> int:
        result = 0
        right = {}
        for c in s:
            if c not in right:
                right[c] = 0
            right[c] += 1
        unique_right = len(right)
        left = {}
        for c in s:
            if c not in left:
                left[c] = 0
            left[c] += 1
            unique_left = len(left)
            right[c] -= 1
            if right[c] == 0:
                unique_right -= 1
            if unique_left == unique_right:
                result += 1
            if unique_left > unique_right:
                break
        return result