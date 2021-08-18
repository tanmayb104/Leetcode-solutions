class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(m)
        c=len(m[0])
        flag=0
        for i in range(r):
            for j in range(c):
                if(m[i][j]==0):
                    flag=1
                    k=i
                    l=j
                    break
        if(not flag):
            return m
        for i in range(r):
            for j in range(c):
                if(m[i][j]==0):
                    m[i][l]=0
                    m[k][j]=0
        # print(m,l,k)
        for i in range(r):
            for j in range(c):
                if((m[i][l]==0 or m[k][j]==0) and not (i==k or j==l)):
                    m[i][j]=0
        # print(m,l,k)
        for i in range(r):
            m[i][l]=0
        for i in range(c):
            m[k][i]=0
        return m
                
        
        