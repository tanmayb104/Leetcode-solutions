class Solution:
    def uniquePathsWithObstacles(self, o: List[List[int]]) -> int:
        n=len(o)
        m=len(o[0])
        l=[1,0]
        for i in range(n):
            for j in range(m):
                o[i][j]=l[o[i][j]]
        flag=True
        for i in range(m):
            if(flag and o[0][i]==1):
                o[0][i]=1
            else:
                flag=False
                o[0][i]=0
        flag=True
        for i in range(n):
            if(flag and o[i][0]==1):
                o[i][0]=1
            else:
                flag=False
                o[i][0]=0
        # print(o)
        for i in range(1,n):
            for j in range(1,m):
                if(o[i][j]==1):
                    o[i][j]=o[i-1][j]+o[i][j-1]
        # print(o)
        return o[n-1][m-1]