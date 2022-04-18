class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        x=[0,0,1,-1]
        y=[1,-1,0,0]
        vis=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(not vis[i][j] and grid[i][j]=="1"):
                    ans+=1
                    st=[[i,j]]
                    vis[i][j]=True
                    while(st):
                        # print(st,ans)
                        s_a,s_b=st.pop()
                        for k in range(4):
                            a=s_a+x[k]
                            b=s_b+y[k]
                            if(a>-1 and a<len(grid) and b>-1 and b<len(grid[0]) and grid[a][b]=="1" and not vis[a][b]):
                                # print(a,b)
                                st.append([a,b])
                                vis[a][b]=True
        return ans