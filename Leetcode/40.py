from copy import copy

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur = []
        result = []
        
        def backtrack(start, cur_sum):
            if cur_sum == target:
                result.append(copy(cur))
            if cur_sum >= target:
                return
            for i in range(start, len(candidates)):
                ith = candidates[i]
                if i > start and ith == candidates[i-1]:
                    continue
                cur.append(ith)
                backtrack(i+1, cur_sum + ith)
                cur.pop()
                
        backtrack(0, 0)
        return result