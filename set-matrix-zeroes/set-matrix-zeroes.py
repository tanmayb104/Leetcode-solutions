class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(m)
        c=len(m[0])
        p=[[m[i][j] for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if(m[i][j]==0):
                    for k in range(c):
                        p[i][k]=0
                    for k in range(r):
                        p[k][j]=0
        for i in range(r):
            for j in range(c):
                m[i][j]=p[i][j]
            
                
        
        