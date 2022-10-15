class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i, prev, prev_cnt, k):
            if k < 0: return inf
            if i == len(s): return 0
            delete = dp(i + 1, prev, prev_cnt, k - 1)
            if s[i] == prev:
                keep = dp(i + 1, prev, prev_cnt + 1, k)
                if prev_cnt in [1, 9, 99]:
                    keep += 1
            else:
                keep = dp(i + 1, s[i], 1, k) + 1
            return min(delete, keep)
        return dp(0, "", 0, k)