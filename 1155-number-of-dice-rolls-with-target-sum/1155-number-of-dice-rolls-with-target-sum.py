class Solution:
    def numRollsToTarget(self, n: int, k: int, t: int) -> int:
        @cache
        def rec(i,t):
            if(i==n and t==0):
                return 1
            elif(t<n-i):
                return 0
            elif((n-i)*k<t):
                return 0
            elif(i==n):
                return 0
            elif(t<0):
                return 0
            else:
                ans=0
                for j in range(1,k+1):
                    ans+=rec(i+1,t-j)
                return ans%(10**9+7)
        return rec(0,t)%(10**9+7)
        