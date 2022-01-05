class Solution:
    def rec(self,nu,data,st,k,ans,pos):
        # print(data,ans)
        if(pos==k):
            ans.append(data[:])
            return
        if(st==len(nu)):
            return
        data[pos]=nu[st]
        self.rec(nu,data,st+1,k,ans,pos+1)
        data[pos]=-1
        self.rec(nu,data,st+1,k,ans,pos)
        
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        nu=[i for i in range(1,n+1)]
        data=[-1 for i in range(k)]
        ans=[]
        self.rec(nu,data,0,k,ans,0)
        return ans