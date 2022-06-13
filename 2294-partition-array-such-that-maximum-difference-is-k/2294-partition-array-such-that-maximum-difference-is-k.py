class Solution:
    def partitionArray(self, n: List[int], k: int) -> int:
        n.sort()
        if(not n):
            return 0
        ans=1
        ma=n[0]
        mi=n[0]
        i=1
        while(i<len(n)):
            ma=max(ma,n[i])
            mi=min(mi,n[i])
            if(ma-mi>k):
                ans+=1
                ma=n[i]
                mi=n[i]
            i+=1
        return ans