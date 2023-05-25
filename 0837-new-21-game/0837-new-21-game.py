class Solution:
    def new21Game(self, N, K, maxPts):
        if K == 0:
            return 1.0
        if N >= K - 1 + maxPts:
            return 1.0

        dp = [0.0] * (N + 1)

        probability = 0.0  
        windowSum = 1.0  
        dp[0] = 1.0
        for i in range(1, N + 1):
            dp[i] = windowSum / maxPts

            if i < K:
                windowSum += dp[i]
            else:
                probability += dp[i]

            if i >= maxPts:
                windowSum -= dp[i - maxPts]

        return probability