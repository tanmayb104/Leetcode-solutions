class Solution:
    def removeStones(self, st: List[List[int]]) -> int:
        r=set()
        c=set()
        p=[i for i in range(len(st))]
        s=[1 for i in range(len(st))]
        m1=0
        m2=0
        for i in st:
            m1=max(m1,i[0])
            m2=max(m2,i[1])
        d1={}
        d2={}
        # print(m1,m2)
        for i in range(m1+1):
            d1[i]=set()
            
        for i in range(m2+1):
            d2[i]=set()
        
        
        def parent(u):
            if(u==p[u]):
                return u
            p[u]=parent(p[u])
            return p[u]
        
        def union(u,v):
            a=parent(u)
            b=parent(v)
            if(a!=b):
                if(s[a]<s[b]):
                    a,b=b,a
                p[b]=a
                s[a]+=s[b]
                
        point=0
        for i in st:
            if(i[0] in r):
                for j in d1[i[0]]:
                    union(point,j)
                    break
                    
            if(i[1] in c):
                for j in d2[i[1]]:
                    union(point,j)
                    break
            d1[i[0]].add(point)
            d2[i[1]].add(point)
            # print(p)
            r.add(i[0])
            c.add(i[1])
            point+=1
        # print(p)
        ans=0
        for i in range(len(p)):
            if(p[i]==i):
                ans+=1
        return len(st)-ans