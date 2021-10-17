class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points:
            d2 = -(x**2 + y**2)
            heappush(pq, [d2, x, y])
            if len(pq) > k:
                heappop(pq)
        return list(map(lambda l: [l[1], l[2]], pq))
                