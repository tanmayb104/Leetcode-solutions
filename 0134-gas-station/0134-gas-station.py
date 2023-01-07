class Solution:
    def canCompleteCircuit(self, g: List[int], c: List[int]) -> int:
        l=[]
        for i in range(len(g)):
            l.append(g[i]-c[i])
        if(sum(l)<0):
            return -1
        m=l[0]
        cu=l[0]
        j=0
        for i in range(1,len(l)):
            if(cu+l[i]<l[i]):
                j=i
                cu=l[i]
            else:
                cu+=l[i]                
            if(cu>m):
                m=cu
        return j