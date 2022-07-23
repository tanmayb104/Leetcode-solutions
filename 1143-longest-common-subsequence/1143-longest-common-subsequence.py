class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        d={}
        def rec(i1,i2):
            tu=tuple([i1,i2])
            if(i1==len(t1) or i2==len(t2)):
                return 0
            if(tu in d):
                return d[tu]
            if(t1[i1]==t2[i2]):
                d[tu]=1+rec(i1+1,i2+1)
                return d[tu]
            d[tu]=max(rec(i1+1,i2),rec(i1,i2+1))
            return d[tu]
        return rec(0,0)