class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[1] * 5] + [[0] * (5) for _ in range(n - 1)]
        moduler = math.pow(10, 9) + 7
        for i in range(1, n):
            for j in range(5):
                if j == 0:
                    dp[i][j] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
                elif j == 1:
                    dp[i][j] = dp[i - 1][0] + dp[i - 1][2]
                elif j == 2:
                    dp[i][j] = dp[i - 1][1] + dp[i - 1][3]
                elif j == 3:
                    dp[i][j] = dp[i - 1][2]
                else:
                    dp[i][j] = dp[i - 1][2] + dp[i - 1][3]
                    
                dp[i][j] = dp[i][j] % moduler

        return int(sum(dp[-1]) % moduler)