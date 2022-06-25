from heapq import *
class Solution:
    def isPossible(self, t: List[int]) -> bool:
        if(len(t)==1):
            if(t[0]==1):
                return True
            else:
                return False
        s=sum(t)
        for i in range(len(t)):
            t[i]=-t[i]
        heapify(t)
        while(len(t)):
            # print(t)
            a=-heappop(t)
            if(a==1):
                continue
            q=s-a
            a-=1
            r=a%q
            v=a//q
            # print(s,r)
            if(q>=a+1):
                return False
            if(r==0):
                s-=a-r
                continue
            elif(r>0):
                s-=a-r
                heappush(t,-r-1)
            else:
                return False
        return True
            