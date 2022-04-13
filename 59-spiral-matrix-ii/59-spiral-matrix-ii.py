class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top=0
        bottom=n-1
        left=0
        right=n-1
        dire=0
        ans=[[0 for i in range(n)] for j in range(n)]
        e=1
        while(top<=bottom and left<=right):
            if(dire==0):
                for i in range(left,right+1):
                    ans[top][i]=e
                    e+=1
                top+=1
            elif(dire==1):
                for i in range(top,bottom+1):
                    ans[i][right]=e
                    e+=1
                right-=1
            elif(dire==2):
                for i in range(right,left-1,-1):
                    ans[bottom][i]=e
                    e+=1
                bottom-=1
            else:
                for i in range(bottom,top-1,-1):
                    ans[i][left]=e
                    e+=1
                left+=1
            dire+=1
            dire%=4
        return ans