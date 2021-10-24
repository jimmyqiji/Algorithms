class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def valid(mid):
            valid = False
            completed_bouquets = 0
            group = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    group += 1
                else:
                    group = 0
                if group == k:
                    completed_bouquets += 1
                    group = 0
                if completed_bouquets >= m:
                    valid = True
                    break
            return valid
        
        lo = min(bloomDay)
        hi = maxhi = max(bloomDay)
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if valid(mid):
                hi = mid
            else:
                lo = mid + 1
        if valid(lo):
            return lo
        return -1