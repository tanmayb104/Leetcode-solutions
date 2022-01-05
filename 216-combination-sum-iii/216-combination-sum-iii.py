class Solution:
    def rec(self,k,n,nu,ans,temp,i):
        if(k==0 and n==0):
            ans.append(temp)
        elif(k==0 or n==0 or i==9):
            return
        else:
            self.rec(k-1,n-nu[i],nu,ans,temp+[nu[i]],i+1)
            self.rec(k,n,nu,ans,temp,i+1)
        
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nu=[i for i in range(1,10)]
        ans=[]
        temp=[]
        self.rec(k,n,nu,ans,temp,0)
        return ans