class NumMatrix:

    def __init__(self, ma: List[List[int]]):
        self.n=len(ma)
        self.m=len(ma[0])
        self.pre=[[ma[i][j] for j in range(self.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(1,self.m):
                self.pre[i][j]+=self.pre[i][j-1]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans=0
        for i in range(row1,row2+1):
            if(col1==0):
                ans+=self.pre[i][col2]
            else:
                ans+=self.pre[i][col2]-self.pre[i][col1-1]
        return ans

                


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)