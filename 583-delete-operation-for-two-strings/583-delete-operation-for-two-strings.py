class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        
        L1, L2 = len(w1), len(w2)
        @lru_cache()
        def solve(i, j):
            if i == L1 and j == L2 : return 0
            if i == L1 or j == L2 : 
                return max(L1 - i, L2 - j)
            if w1[i] == w2[j] : 
                return solve(i + 1, j + 1)                
            return 1 + min(solve(i + 1, j), solve(i, j + 1))    
        
        return solve(0, 0) 