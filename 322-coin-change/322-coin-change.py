class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1 for i in range(amount+1)]
        dp[0]=0
        for i in range(len(coins)):
            if(coins[i]<amount+1):
                dp[coins[i]]=1
        for i in range(amount+1):
            if(dp[i]!=-1):
                for j in range(len(coins)):
                    a=i+coins[j]
                    if(a<amount+1):
                        if(dp[a]!=-1):
                            dp[a]=min(dp[a],dp[i]+1)
                        else:
                            dp[a]=dp[i]+1
        return dp[amount]
                