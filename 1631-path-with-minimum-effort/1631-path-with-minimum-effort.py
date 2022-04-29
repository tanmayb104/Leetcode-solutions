from heapq import *
class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        n=len(h)
        m=len(h[0])
        l=[]
        heapify(l)
        heappush(l,tuple([0,0,0]))
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        vis=[[False for i in range(m)] for j in range(n)]
        while(l):
            # print(l)
            a,b,c=heappop(l)
            if(vis[b][c]):
                continue
            if(b==n-1 and c==m-1):
                return a
            vis[b][c]=True
            for i in range(4):
                sb=b+x[i]
                sc=c+y[i]
                if(sb>-1 and sc>-1 and sb<n and sc<m and not vis[sb][sc]):
                    sa=max(a,abs(h[sb][sc]-h[b][c]))
                    heappush(l,tuple([sa,sb,sc]))
        return