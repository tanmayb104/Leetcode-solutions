class Solution:
    def makesquare(self, m: List[int]) -> bool:
        s=sum(m)
        if(s%4!=0):
            return False
        p=s//4
        m.sort(reverse=True)
        if(m[0]>p):
            return False
        @lru_cache()
        def rec(i,s1,s2,s3,s4):
            if(i==len(m)):
                if(s1==p and s2==p and s3==p and s4==p):
                    return True
                else:
                    return False
            a1=False
            a2=False
            a3=False
            a4=False
            if(s1+m[i]<=p):
                a1=rec(i+1,s1+m[i],s2,s3,s4)
            if(s2+m[i]<=p):
                a2=rec(i+1,s1,s2+m[i],s3,s4)
            if(s3+m[i]<=p):
                a3=rec(i+1,s1,s2,s3+m[i],s4)
            if(s4+m[i]<=p):
                a4=rec(i+1,s1,s2,s3,s4+m[i])
            return  a1 or a2 or a3 or a4
        return rec(0,0,0,0,0)
                    
                    