class Solution:
    def numDecodings(self, s: str) -> int:
        if(s[0]=="0"):
            return 0
        dp=[0 for i in range(len(s)+1)]
        dp[0]=1
        dp[1]=1
        if(len(s)<2):
            return dp[len(s)]
        for i in range(2,len(s)+1):
            if(s[i-1]=="0"):
                if(int(s[i-2])==0 or int(s[i-2])>2):
                    return 0
                else:
                    dp[i]=dp[i-2]
            else:
                temp=int(s[i-2:i])
                if(len(str(temp))==2 and temp<27):
                    dp[i]=dp[i-1]+dp[i-2]
                else:
                    dp[i]=dp[i-1]
        # print(dp)
        return dp[-1]