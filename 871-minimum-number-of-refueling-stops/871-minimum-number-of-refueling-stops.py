from heapq import *
class Solution:
    def minRefuelStops(self, t: int, s: int, st: List[List[int]]) -> int:
    
        h=[]
        st+=[[t,0]]
        heapify(h)
        pos=0
        ans=0
        i=0
        while(i<len(st)):
            # print(pos,s,h)
            if(s>=st[i][0]-pos):
                s-=st[i][0]-pos
                heappush(h,-st[i][1])
                pos=st[i][0]
                i+=1
            elif(h):
                while(h and s<st[i][0]-pos):
                    ans+=1
                    a=heappop(h)
                    s-=a
            else:
                break
        if(i==len(st)):
            return ans
        return -1