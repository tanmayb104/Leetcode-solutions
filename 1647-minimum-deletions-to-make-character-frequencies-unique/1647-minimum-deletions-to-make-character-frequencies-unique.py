class Solution:
    def minDeletions(self, s: str) -> int:
        ans=0
        l=sorted(Counter(s).values(),reverse=True)
        mi=999999999999999999
        for v in l:
            if(v<mi):
                mi=v
            elif(v==mi):
                ans+=1
                mi-=1
            elif(mi==0):
                ans+=v
            else:
                ans+=v-mi+1
                mi-=1
        return ans