class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        mid = total // 2
        dp = [[0 for _ in range(mid+1)] for _ in range(len(stones)+1)]
        # dp[i][j] is max weight below j using first i stones
        
        for i in range(1, len(stones)+1):
            # only using first i stones
            for cap in range(1, mid+1):
                if stones[i-1] <= cap:
                    dp[i][cap] = max(dp[i-1][cap], stones[i-1] + dp[i-1][cap-stones[i-1]])
                else:
                    dp[i][cap] = dp[i-1][cap]
        return total - 2*dp[-1][-1]