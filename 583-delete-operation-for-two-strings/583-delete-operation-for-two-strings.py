class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[1000]*(len(w2)+1) for i in range(2)]
        for i in range(len(w1) + 1):
            for j in range(len(w2) + 1):
                dp[i & 1][j] = i + j if i == 0 or j == 0 else dp[(i - 1) & 1][j - 1] if w1[i - 1] == w2[j - 1] else 1 + min(dp[(i - 1) & 1][j], dp[i & 1][j - 1])
        return dp[len(w1) & 1][-1]