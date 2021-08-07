class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi=999999999999999
        ans=0
        for i in prices:
            mi=min(mi,i)
            ans=max(i-mi,ans)
        return ans