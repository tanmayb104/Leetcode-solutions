class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        n=len(g)
        m=len(g[0])
        vis=[[False for i in range(m)] for j in range(n)]
        ans=0
        x=[1,-1,0,0]
        y=[0,0,-1,1]
        for i in range(n):
            for j in range(m):
                if(g[i][j]==1 and not vis[i][j]):
                    q=[[i,j]]
                    area=0
                    while(q):
                        a,b=q.pop()
                        if(not vis[a][b]):
                            vis[a][b]=True
                            area+=1
                            for k in range(4):
                                sa=a+x[k]
                                sb=b+y[k]
                                if(sa>-1 and sa<n and sb>-1 and sb<m and not vis[sa][sb] and g[sa][sb]==1):
                                    q.append([sa,sb])
                    ans=max(ans,area)
        return ans
                                
                            
                            