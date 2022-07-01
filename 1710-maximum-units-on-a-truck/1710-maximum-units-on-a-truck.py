class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], t: int) -> int:
        b=sorted(boxTypes,key=lambda x:-x[1])
        i=0
        ans=0
        while(t and i<len(b)):
            if(b[i][0]<t):
                ans+=b[i][0]*b[i][1]
                t-=b[i][0]
            else:
                ans+=t*b[i][1]
                t=0
            i+=1
        return ans