class Solution:
    def longestPalindromeSubseq(self, s1: str) -> int:
        s2=s1[::-1]
        d={}
        def rec(i1,i2):
            if(i1==len(s1) or i2==len(s2)):
                return 0
            tu=tuple([i1,i2])
            if(tu in d):
                return d[tu]
            if(s1[i1]==s2[i2]):
                d[tu]=1+rec(i1+1,i2+1)
                return d[tu]
            d[tu]=max(rec(i1,i2+1),rec(i1+1,i2))
            return d[tu]
        
        return rec(0,0)
            
            