class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, b: str) -> str:
        d={}
        for i in set(s1+s2+b):
            d[i]=i
        def par(u):
            if(d[u]!=u):
                d[u]=par(d[u])
            return d[u]
        def union(u,v):
            pu=par(u)
            pv=par(v)
            if(pu!=pv):
                if(pu>pv):
                    pu,pv=pv,pu
                d[pv]=pu
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans=""
        for i in range(len(b)):
            pi=par(b[i])
            ans+=pi
        return ans