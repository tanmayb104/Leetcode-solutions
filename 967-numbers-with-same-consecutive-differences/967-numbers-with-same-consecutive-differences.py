class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans=[]
        @lru_cache()
        def rec(n,k,i,s):
            if(i==n):
                ans.append(s)
                # print(s)
            else:
                if(int(s[-1])+k<10):
                    rec(n,k,i+1,s+str(int(s[-1])+k))
                if(int(s[-1])-k>-1 and k!=0):
                    rec(n,k,i+1,s+str(int(s[-1])-k))
        for i in range(1,10):
            rec(n,k,1,str(i))
        return ans