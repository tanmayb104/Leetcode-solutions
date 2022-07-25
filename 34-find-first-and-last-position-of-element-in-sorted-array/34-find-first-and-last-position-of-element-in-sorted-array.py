class Solution:
    def searchRange(self, n: List[int], t: int) -> List[int]:
        if(not n):
            return [-1,-1]
        l=0
        r=len(n)-1
        while(l<r):
            mid=(l+r)//2
            if(n[mid]==t):
                r=mid
            elif(n[mid]<t):
                l=mid+1
            else:
                r=mid-1
        le=l
        if(le<len(n) and n[le]!=t):
            return [-1,-1]
        l=0
        r=len(n)-1
        while(l<r):
            mid=(l+r)//2
            if(n[mid]==t):
                l=mid
                if(l==r-1):
                    if(n[r]==t):
                        l=r
                    else:
                        break
            elif(n[mid]<t):
                l=mid+1
            else:
                r=mid-1
        return [le,l]