class Solution:
    def rec(self, c,t,i,ans,temp,s):
        # print(temp,ans)
        if(t==0 and tuple(temp) not in s):
            ans.append(temp)
            s.add(tuple(temp))
        if(i==len(c) or t<=0):
            return
        self.rec(c,t-c[i],i,ans,temp+[c[i]],s)
        self.rec(c,t,i+1,ans,temp,s)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]
        s=set()
        self.rec(candidates,target,0,ans,temp,s)
        return ans