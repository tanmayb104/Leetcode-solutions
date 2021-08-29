class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        if(len(p)==0):
            return 0
        p=sorted(p,key=lambda x:x[1])
        ans=1
        cur=p[0][1]
        for i in range(1,len(p)):
            if(p[i][0]<=cur):
                continue
            else:
                ans+=1
                cur=p[i][1]
        return ans
                    
        