class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def nextInd(j):
            res = (j+nums[j]) % len(nums)
            if res < 0:
                res += len(nums)
            return res
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            walker = runner = i
            while nums[runner] * nums[nextInd(runner)] > 0 and nums[runner] * nums[nextInd(nextInd(runner))] > 0:
                walker = nextInd(walker)
                runner = nextInd(nextInd(runner))
                if walker == runner:
                    if runner == nextInd(runner):
                        break
                    return True
            walker = i
            nextwalker = nextInd(walker)
            while nums[walker] * nums[nextwalker] > 0:
                nums[walker] = 0
                walker = nextwalker
        return False