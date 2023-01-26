class Solution:
    def findCheapestPrice(self, n: int, f: List[List[int]], src: int, dst: int, k: int) -> int:
        g={}
        d={}
        for i in range(n):
            g[i]=[]
            d[i]=n
        for i in f:
            g[i[0]].append(i[1:])
        h=[[0,src,-1]]
        heapify(h)
        while(h):
            a=heappop(h)
            if(a[1]==dst):
                return a[0]
            elif(a[2]<k and d[a[1]]>a[2]):
                d[a[1]]=a[2]
                for i in g[a[1]]:
                    heappush(h,[a[0]+i[1],i[0],a[2]+1])
        return -1
                    
                    
            