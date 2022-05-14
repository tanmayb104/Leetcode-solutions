from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g={}
        for i in range(1,n+1):
            g[i]=[]
        for i in range(len(times)):
            g[times[i][0]].append([times[i][1],times[i][2]])
        vis=[False for i in range(n+1)]
        st=[[0,k]]
        heapify(st)
        ans=-9999999999
        # print(g)
        while(st):
            # print(st,vis)
            b,a=heappop(st)
            # print(a,b)
            if(not vis[a]):
                vis[a]=True
                ans=max(b,ans)
                for i in range(len(g[a])):
                    if(not vis[g[a][i][0]]):
                        heappush(st,[b+g[a][i][1],g[a][i][0]])
        for i in range(1,n+1):
            if(not vis[i]):
                return -1
        return ans
            