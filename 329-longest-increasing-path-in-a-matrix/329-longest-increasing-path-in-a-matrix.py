from heapq import *
class Solution:
    def longestIncreasingPath(self, ma: List[List[int]]) -> int:
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        h=[]
        heapify(h)
        n=len(ma)
        m=len(ma[0])
        for i in range(n):
            for j in range(m):
                heappush(h,[-ma[i][j],i,j])
        l=[[0 for i in range(m)] for j in range(n)]
        maxim=0
        while(h):
            a,b,c=heappop(h)
            maxi=0
            for i in range(4):
                sb=b+x[i]
                sc=c+y[i]
                if(0<=sb<n and 0<=sc<m and ma[b][c]<ma[sb][sc]):
                    maxi=max(maxi,l[sb][sc])
            l[b][c]=maxi+1
            maxim=max(maxim,l[b][c])
        # print(l)
        return maxim
                    