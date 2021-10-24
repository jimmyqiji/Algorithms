class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = [nums[0]]
        for i in range(1, len(nums)):
            if subseq[-1] < nums[i]:
                subseq.append(nums[i])
                continue
            ind = bisect_left(subseq, nums[i])
            subseq[ind] = nums[i]
        return len(subseq)