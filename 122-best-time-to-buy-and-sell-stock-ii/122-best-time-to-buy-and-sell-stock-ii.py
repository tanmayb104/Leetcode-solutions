class Solution:
    def maxProfit(self, p: List[int]) -> int:
        ans=0
        for i in range(len(p)-1):
            if(p[i]<p[i+1]):
                ans+=p[i+1]-p[i]
        return ans