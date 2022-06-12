class Solution:
    def maximumUniqueSubarray(self, n: List[int]) -> int:
        ans=0
        d={}
        l=-1
        pre=[0]
        for i in range(len(n)):
            pre.append(pre[-1]+n[i])
        for i in range(len(n)):
            if(n[i] in d):
                l=max(l,d[n[i]])
                d[n[i]]=i
            else:
                d[n[i]]=i
            ans=max(ans,pre[i+1]-pre[l+1])
        return ans
                