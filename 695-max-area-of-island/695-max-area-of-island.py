class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        n=len(g)
        m=len(g[0])
        x=[1,0]
        y=[0,1]
        
        p=[0 for i in range(n*m)]
        r=[0 for i in range(n*m)]
        for i in range(n):
            for j in range(m):
                p[i*m+j]=i*m+j
                if(g[i][j]==1):
                    r[i*m+j]=1
                
        def find_set(a):
            if(a==p[a]):
                return a
            p[a]=find_set(p[a])
            return p[a]
        
        def union_set(a,b):
            a=find_set(a)
            b=find_set(b)
            if(a!=b):
                if(r[a]<r[b]):
                    a,b=b,a
                p[b]=a
                r[a]+=r[b]
        
        for i in range(n):
            for j in range(m):
                if(g[i][j]==1):
                    for k in range(2):
                        sa=i+x[k]
                        sb=j+y[k]
                        if(sa>-1 and sa<n and sb>-1 and sb<m and g[sa][sb]==1):
                            union_set(i*m+j,sa*m+sb)
        
        return max(r)
                                
                            
                            