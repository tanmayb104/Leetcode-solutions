class Solution:
    def totalFruit(self, f: List[int]) -> int:
        l=0
        d={}
        r=0
        t=0
        ans=0
        while(r<len(f)):
            if(f[r] in d):
                if(d[f[r]]==0):
                    t+=1
                d[f[r]]+=1                    
            else:
                d[f[r]]=1
                t+=1
            while(t>2):
                d[f[l]]-=1
                if(d[f[l]]==0):
                    t-=1
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans