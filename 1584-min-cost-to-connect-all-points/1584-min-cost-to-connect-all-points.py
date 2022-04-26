class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d={}
        for i in points:
            d[str(i[0])+","+str(i[1])]=999999999999999
        vis=set()
        d[str(points[0][0])+","+str(points[0][1])]=0
        ans=0
        while(len(vis)<len(points)):
            a,b=999999999999999,0
            for i in points:
                c=str(i[0])+","+str(i[1])
                if(c not in vis):
                    if(a>d[c]):
                        a=d[c]
                        b=c
            vis.add(b)
            ans+=d[b]
            point=b.split(",")
            for i in points:
                c=str(i[0])+","+str(i[1])
                if(c not in vis):
                    d[c]=min(d[c],abs(i[0]-int(point[0]))+abs(i[1]-int(point[1])))
        return ans
                
            