class Solution:
    def rec(self, c,t,i,ans,temp,s):
        # print(temp,ans)
        if(t==0 and tuple(temp) not in s):
            ans.append(temp)
            s.add(tuple(temp))
        if(i==len(c) or t<=0):
            return
        self.rec(c,t-c[i],i+1,ans,temp+[c[i]],s)
        while(i+1<len(c) and c[i]==c[i+1]):
            i+=1
        self.rec(c,t,i+1,ans,temp,s)
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        temp=[]
        s=set()
        self.rec(candidates,target,0,ans,temp,s)
        return ans