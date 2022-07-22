class Solution:
    def coinChange(self, c: List[int], a: int) -> int:
        c.sort()
        d={}
        def rec(i,a):
            tu=tuple([i,a])
            if(a==0):
                return 0
            if(i==len(c)):
                return 9999999999999999
            if(tu in d):
                return d[tu]
            if(c[i]<=a):
                d[tu]=min(1+rec(i,a-c[i]),rec(i+1,a))
                return d[tu]
            return 9999999999999999
        
        ans=rec(0,a)
        if(ans>=9999999999999999):
            return -1
        return ans