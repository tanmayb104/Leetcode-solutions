class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ze=s.count("0")
        on=s.count("1")
        l=[]
        for i in range(len(s)):
            if(s[i]=="0"):
                l.append(1)
            else:
                l.append(0)
        for i in range(1,len(l)):
            l[i]+=l[i-1]
        ans=min(ze,on)
        for i in range(len(l)):
            p=i+1
            ans=min(ans,p-l[i]+ze-l[i])
        return ans
        