class Solution:
    def longestIncreasingPath(self, ma: List[List[int]]) -> int:
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        n=len(ma)
        m=len(ma[0])
        dp=[[0 for i in range(m)] for j in range(n)]
        
        def rec(b,c):
            l=0
            if(dp[b][c]):
                return dp[b][c]
            for i in range(4):
                sb=b+x[i]
                sc=c+y[i]
                if(0<=sb<n and 0<=sc<m and ma[b][c]<ma[sb][sc]):
                    l=max(l,rec(sb,sc))
            dp[b][c]=1+l
            return dp[b][c]
        
        maxi=0
        for i in range(n):
            for j in range(m):
                dp[i][j]=rec(i,j)
                maxi=max(maxi,dp[i][j])
        return maxi