class Solution:
    def minCost(self, c: str, n: List[int]) -> int:
        l=0
        ans=0
        if(len(c)==1):
            return 0
        for i in range(1,len(c)):
            if(c[i]==c[l]):
                if(n[i]>=n[l]):
                    ans+=n[l]
                    l=i
                else:
                    ans+=n[i]
            else:
                l=i
        return ans