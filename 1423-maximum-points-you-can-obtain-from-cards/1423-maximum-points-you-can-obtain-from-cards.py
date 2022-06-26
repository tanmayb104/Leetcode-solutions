class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        n=len(c)
        s=0
        for i in range(n-k):
            s+=c[i]
        l=0
        r=n-k
        ans=s
        while(r<n):
            s+=c[r]
            s-=c[l]
            ans=min(s,ans)
            l+=1
            r+=1
        return sum(c)-ans