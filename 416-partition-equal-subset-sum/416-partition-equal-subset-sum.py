class Solution:
    def canPartition(self, n: List[int]) -> bool:
        s=sum(n)
        d={}
        def rec(i,s):
            a=tuple([i,s])
            if(s==0):
                return True
            if(i==len(n)):
                return False
            if(a in d):
                return d[a]
            if(n[i]<=s):
                d[a]=rec(i+1,s-n[i]) or rec(i+1,s)
                return d[a]
            d[a]=rec(i+1,s)
            return d[a]
        if(s%2==0):
            return rec(0,s//2)
        return False