from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if(grid[0][0]==1):
            return -1
        st=deque([[0,0,1]])
        n=len(grid)
        vis=[[False for i in range(n)] for j in range(n)]
        ans=9999999999999999
        x=[-1,-1,0,1,1,1,0,-1]
        y=[0,-1,-1,-1,0,1,1,1]
        while(st):
            a,b,c=st.popleft()
            if(vis[a][b]):
                continue
            vis[a][b]=True
            if(a==n-1 and b==n-1):
                ans=min(ans,c)
            else:
                for i in range(8):
                    sa=a+x[i]
                    sb=b+y[i]
                    if(sa>-1 and sa<n and sb>-1 and sb<n and not vis[sa][sb] and grid[sa][sb]==0):
                        st.append([sa,sb,c+1])
        if(ans==9999999999999999):
            return -1
        return ans