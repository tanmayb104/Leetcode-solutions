class Solution:
    def minCostClimbingStairs(self, c: List[int]) -> int:
        c=[0]+c+[0]
        ans=[0 for i in range(len(c))]
        ans[1]=c[1]
        for i in range(2,len(c)):
            ans[i]=c[i]+min(ans[i-1],ans[i-2])
        return(ans[-1])