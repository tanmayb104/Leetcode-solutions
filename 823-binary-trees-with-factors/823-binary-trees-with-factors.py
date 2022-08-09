class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        arr.sort()
        MOD = 10**9 + 7
        
        # create a dictionary and initialize
        dp = {}
        for n in arr:
            dp[n] = 1
            
        # loop through each number
        for i, n in enumerate(arr):
            for j in range(i):
                if not(n % arr[j]) and n // arr[j] in dp:
                    dp[n] += dp[arr[j]] * dp[n//arr[j]]
                    dp[n] %= MOD
        
        return sum(dp.values()) % MOD