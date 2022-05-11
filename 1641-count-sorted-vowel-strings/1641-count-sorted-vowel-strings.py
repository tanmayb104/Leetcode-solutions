class Solution:
    
    def countVowelStrings(self, n: int) -> int:
        dp=[[0 for i in range(n)] for j in range(6)]
        # for i in dp:
        #     print(*i)
        dp[1][0]=1
        dp[2][0]=2
        dp[3][0]=3
        dp[4][0]=4
        dp[5][0]=5
        for j in range(1,n):
            for i in range(1,6):
                # print(i,j)
                dp[i][j]+=dp[i-1][j]+dp[5][j-1]-dp[i-1][j-1]
        # for i in dp:
        #     print(*i)
        return dp[5][n-1]