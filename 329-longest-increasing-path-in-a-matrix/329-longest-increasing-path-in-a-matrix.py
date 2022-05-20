class Solution:
    def longestIncreasingPath(self, ma: List[List[int]]) -> int:
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        n=len(ma)
        m=len(ma[0])
        
        @lru_cache(maxsize=50000)
        def rec(b,c):
            l=0
            for i in range(4):
                sb=b+x[i]
                sc=c+y[i]
                if(0<=sb<n and 0<=sc<m and ma[b][c]<ma[sb][sc]):
                    l=max(l,rec(sb,sc))
            return 1+l
        
        maxi=0
        for i in range(n):
            for j in range(m):
                maxi=max(maxi,rec(i,j))
        return maxi