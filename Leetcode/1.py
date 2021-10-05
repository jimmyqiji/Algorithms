class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = [i]
            else:
                map[nums[i]].append(i)
        for i in range(len(nums)):
            if (target-nums[i] in map and map[target-nums[i]][0] != i):
                return [i, map[target-nums[i]][0]]
            