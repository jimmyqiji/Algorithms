class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        result = []
        for i in range(min(k, len(nums1))):
            heappush(heap, [nums1[i]+nums2[0], nums1[i], nums2[0], 0])
        while len(heap) > 0 and len(result) < k:
            [_, a, b, i2] = heappop(heap)
            result.append([a,b])
            if i2 + 1 < len(nums2):
                heappush(heap, [a+nums2[i2+1], a, nums2[i2+1], i2+1])
        return result