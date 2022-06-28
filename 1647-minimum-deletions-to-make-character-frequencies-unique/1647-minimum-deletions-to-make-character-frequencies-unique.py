class Solution:
    def minDeletions(self, s: str) -> int:
        ans=0
        d={}
        for i in s:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        l=sorted(d.items(),key=lambda x:x[1], reverse=True)
        mi=999999999999999999
        for k,v in l:
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
        if(mi<0):
            return -1
        return ans