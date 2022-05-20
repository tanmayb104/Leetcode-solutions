class Solution:
    def uniquePathsWithObstacles(self, o: List[List[int]]) -> int:
        n=len(o)
        m=len(o[0])
        l=[[0 for i in range(m)] for j in range(n)]
        flag=True
        for i in range(m):
            if(flag and o[0][i]==0):
                l[0][i]=1
            else:
                flag=False
        flag=True
        for i in range(n):
            if(flag and o[i][0]==0):
                l[i][0]=1
            else:
                flag=False
        for i in range(1,n):
            for j in range(1,m):
                if(o[i][j]==0):
                    l[i][j]=l[i-1][j]+l[i][j-1]
        return l[n-1][m-1]