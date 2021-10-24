class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        maxDist = 0
        for house in houses:
            ind = bisect_left(heaters, house)
            dist = inf
            if ind < len(heaters):
                dist = heaters[ind] - house
            if ind-1 >= 0:
                dist = min(dist, house - heaters[ind-1])
            maxDist = max(maxDist, dist)
        return maxDist