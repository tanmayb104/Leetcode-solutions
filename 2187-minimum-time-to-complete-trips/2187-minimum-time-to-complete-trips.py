class Solution:
    def minimumTime(self, t: List[int], to: int) -> int:
        t.sort()
        print(t)
        l=1
        r=to*t[-1]
        while(l<r):
            mid=(l+r)//2
            a=0
            for i in t:
                a+=mid//i
            # print(mid,l,r,a)
            if(a>=to):
                r=mid
            else:
                l=mid+1
        return l