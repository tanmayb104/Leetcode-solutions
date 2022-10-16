class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
    
        @cache
        def dp(i, k):
            if k == d: return max(jobDifficulty[i:])
            res = float('inf')
            cur = 0
            for j in range(i, n - d + k):
                cur = max(cur, jobDifficulty[j])
                res = min(res, cur + dp(j + 1, k + 1))
            return res
        return -1 if n < d else dp(0, 1)