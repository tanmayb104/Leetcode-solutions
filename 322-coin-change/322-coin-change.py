class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @cache
        # def rec(amount,i,count):
        #     if(amount<0 or i==len(coins)):
        #         return 
        #     elif(amount==0):
        #         self.ans=min(count,self.ans)
        #     else:
        #         rec(amount-coins[i],i,count+1)
        #         rec(amount,i+1,count)
        coins=list(set(coins))
        coins.sort(reverse=True)
        # self.ans=999999999999999
        # rec(amount,0,0)
        # if(self.ans==999999999999999):
        #     return -1
        # return self.ans
        
        dp=[0 for i in range(amount+1)]
        # for i in range(len(coins)):
        #     if(coins[i]<amount+1):
        #         dp[coins[i]]=1
        if(not amount):
            return 0
        dp[0]=1
        for i in range(amount+1):
            if(dp[i]>0):
                for j in range(len(coins)):
                    amt=i+coins[j]
                    if(amt<amount+1):
                        if(dp[i+coins[j]]):
                            dp[i+coins[j]]=min(dp[i]+1,dp[i+coins[j]])
                        else:
                            dp[i+coins[j]]=dp[i]+1
        # print(dp)
        if(dp[amount]):
            return dp[amount]-1
        return -1
        
                