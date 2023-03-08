class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        l=1
        r=max(p)
        while(l<r):
            mid=(l+r)//2
            a=0
            for i in p:
                a+=ceil(i/mid)
            # print(a,mid,l,r)
            if(a<=h):
                r=mid
            else:
                l=mid+1
        return l