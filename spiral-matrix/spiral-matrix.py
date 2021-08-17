class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        top=0
        bottom=len(m)-1
        left=0
        right=len(m[0])-1
        dire=0
        ans=[]
        while(top<=bottom and left<=right):
            if(dire==0):
                for i in range(left,right+1):
                    ans.append(m[top][i])
                top+=1
            elif(dire==1):
                for i in range(top,bottom+1):
                    ans.append(m[i][right])
                right-=1
            elif(dire==2):
                for i in range(right,left-1,-1):
                    ans.append(m[bottom][i])
                bottom-=1
            else:
                for i in range(bottom,top-1,-1):
                    ans.append(m[i][left])
                left+=1
            dire+=1
            dire%=4
        return ans
                    