class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        lr=0
        rr=len(m)-1
        while(lr<rr):
            mid=(lr+rr)//2
            if(m[mid][0]<=t and t<=m[mid][-1]):
                lr=mid
                break
            elif(m[mid][0]>t):
                rr=mid-1
            else:
                lr=mid+1
        r=lr
        lr=0
        rr=len(m[0])-1
        while(lr<rr):
            mid=(lr+rr)//2
            if(m[r][mid]==t):
                return True
            elif(m[r][mid]>t):
                rr=mid-1
            else:
                lr=mid+1
        if(m[r][lr]==t):
            return True
        return False