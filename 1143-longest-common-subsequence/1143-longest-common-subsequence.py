class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        d={}
        def rec(i1,i2):
            tu=tuple([i1,i2])
            if(i1==len(t1) or i2==len(t2)):
                return 0
            if(tu in d):
                return d[tu][0]
            if(t1[i1]==t2[i2]):
                d[tu]=[1+rec(i1+1,i2+1),0]
                return d[tu][0]
            a=rec(i1+1,i2)
            b=rec(i1,i2+1)
            if(a>b):
                d[tu]=[a,1]
            else:
                d[tu]=[b,-1]
            return d[tu][0]
        rec(0,0)
        i1=0
        i2=0
        ans=""
        while(i1<len(t1) and i2<len(t2)):
            if(t1[i1]==t2[i2]):
                ans+=t1[i1]
                i1+=1
                i2+=1
            else:
                tu=tuple([i1,i2])
                if(d[tu][1]==1):
                    i1+=1
                else:
                    i2+=1
        print(ans)
        return len(ans)