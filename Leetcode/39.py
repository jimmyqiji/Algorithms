import copy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cur_sum = 0
        result = []
        cur = []
        
        def backtrack(start, cur_sum):
            if cur_sum == target:
                result.append(copy.copy(cur))
            if cur_sum >= target:
                return
            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                cur_sum += candidates[i]
                backtrack(i, cur_sum)
                cur_sum -= candidates[i]
                cur.pop()
                
        backtrack(0, cur_sum)
        return result