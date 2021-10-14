class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        min_4 = [nums[0]]
        max_4 = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            if len(min_4) == 4:
                if num < max(min_4):
                    min_4.remove(max(min_4))
                    min_4.append(num)
                if num > min(max_4):
                    max_4.remove(min(max_4))
                    max_4.append(num)
            else:
                min_4.append(num)
                max_4.append(num)
                
        min_4.sort()
        max_4.sort()
        result = math.inf
        for i in range(0, 4):
            result = min(result, max_4[i] - min_4[i])
        return result