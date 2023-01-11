class Solution:
    def minTime(self, n: int, e: List[List[int]], app: List[bool]) -> int:
        g={}
        for i in e:
            if(i[0] in g):
                g[i[0]].append(i[1])
            else:
                g[i[0]]=[i[1]]
            if(i[1] in g):
                g[i[1]].append(i[0])
            else:
                g[i[1]]=[i[0]]
#         vis=set()
#         ans=0        
#         prev=False
#         prevh=-1
#         def dfs(node,h):
#             if(node):
#                 for i in g[node]:
#                     if(i not in vis):
#                         dfs(i,h+1)
#                 if(a[node]):
#                     if(prev):
                        
#                     else:
#                         prev=True
#                         ans+=h
#                         prevh=h
        
        
        
        
        dep=[-1 for i in range(n)]
        par=[-1 for i in range(n)]
        q=deque([0,-1])
        d=0
        vis=set()
        while(q):
            a=q.popleft()
            if(a==-1 and len(q)):
                d+=1
                q.append(-1)
            elif(a==-1):
                break
            else:
                vis.add(a)
                dep[a]=d
                for i in g[a]:
                    if(i not in vis):
                        par[i]=a
                        q.append(i)
        # print(par)
        # print(dep)
        
        # ans=0
        # h=heapq([])
        # for i in range(n):
        #     if(a[i]):
        #         heappush([-dep[i],i])
        
        vis=set()
        a1=app.copy()
        # print(a1)
        for i in range(1,n):
            if(app[i]):
                while(i!=-1 or i in vis):
                    vis.add(i)
                    i=par[i]
                    if(i!=-1):
                        a1[i]=True
        # print(a1)
        return sum(a1[1:])*2
            
        
        # return 0
            
        