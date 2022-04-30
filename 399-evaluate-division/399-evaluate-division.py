class Solution:
    def calcEquation(self, e: List[List[str]], v: List[float], q: List[List[str]]) -> List[float]:
        g={}
        for i in range(len(e)):
            for j in range(len(e[i])):
                if(e[i][j] not in g):
                    g[e[i][j]]={}
            g[e[i][0]][e[i][1]]=v[i]
            g[e[i][1]][e[i][0]]=1/v[i]
        # print(g)
        
        def rec(a,b,g,ans,vis):
            # print(a,b,ans)
            if(a==b):
                raise Exception(ans)
            p=-1
            vis[a]=True
            for i in g[a].keys():
                if(not vis[i]):
                    rec(i,b,g,ans*g[a][i],vis)
                    
        f=[]
        for i in range(len(q)):
            a,b=q[i]
            # print("1",a,b,f)
            if(a not in g or b not in g):
                f.append(-1)
                continue
            if(a==b):
                f.append(1)
                continue
            ans=1
            vis={i:False for i in g.keys()}
            try:
                rec(a,b,g,ans,vis)
                f.append(-1)
            except Exception as e:
                f.append(e.args[0])
        return f
                
                
            