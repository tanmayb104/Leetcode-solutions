class Solution:
    def longestIncreasingPath(self, ma: List[List[int]]) -> int:
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        n=len(ma)
        m=len(ma[0])
        
        def rec(b,c):
            l=0
            if((b,c) in d):
                return d[(b,c)]
            for i in range(4):
                sb=b+x[i]
                sc=c+y[i]
                if(0<=sb<n and 0<=sc<m and ma[b][c]<ma[sb][sc]):
                    l=max(l,rec(sb,sc))
            d[(b,c)]=1+l
            return 1+l
        
        maxi=0
        d={}
        for i in range(n):
            for j in range(m):
                maxi=max(maxi,rec(i,j))
        # print(d)
        return maxi