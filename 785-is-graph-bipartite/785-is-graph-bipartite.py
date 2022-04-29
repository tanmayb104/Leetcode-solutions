from collections import deque
class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        n=len(g)
        d={i:-1 for i in range(n)}
        vis=[False for i in range(n)]
        for k in range(n):
            if(d[k]==-1):
                d[k]=False
                q=deque([k])
                while(q):
                    a=q.popleft()
                    c=not d[a]
                    vis[a]=True
                    # print(d,a,c)
                    for i in g[a]:
                        if(not vis[i]):
                            q.append(i)
                            if(d[i]==-1):
                                d[i]=c
                            elif(d[i]!=c):
                                return False
                        else:
                            if(d[i]!=c):
                                return False
        return True
                    