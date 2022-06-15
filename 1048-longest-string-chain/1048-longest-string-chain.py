class Solution:
    def longestStrChain(self, w: List[str]) -> int:
        s=set(w)
        w=list(s)
        w=sorted(w,key=lambda x:len(x))
        d={}
        for i in w:
            d[i]=1
        for i in w:
            for j in range(len(i)):
                a=i[:j]+i[j+1:]
                if(a in s):
                    d[i]=max(d[i],d[a]+1)
        ans=0
        print(w)
        print(d)
        for i in w:
            ans=max(ans,d[i])
        return ans