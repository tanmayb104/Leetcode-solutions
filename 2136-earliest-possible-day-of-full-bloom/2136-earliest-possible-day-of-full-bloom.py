class Solution:
    def earliestFullBloom(self, p: List[int], g: List[int]) -> int:
        ans=0
        q=0
        l=[]
        for i in range(len(p)):
            l.append([p[i],g[i]])
        l=sorted(l,key=lambda x:-x[1])
        print(l)
        for i in l:
            q+=i[0]
            ans=max(ans,q+i[1]+1)
        return ans-1