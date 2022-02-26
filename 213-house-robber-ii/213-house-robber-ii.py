class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[] for i in range(n)]
        if(n==1):
            return nums[0]
        elif(n==2):
            return max(nums[0],nums[1])
        elif(n==3):
            return max(nums[0],nums[1],nums[2])
        else:
            dp[0]=[nums[0],1]
            if(nums[0]>nums[1]):
                dp[1]=[nums[0],1]
            else:
                dp[1]=[nums[1],0]
            for i in range(2,n):
                if(dp[i-2][0]+nums[i]>dp[i-1][0]):
                    dp[i]=[dp[i-2][0]+nums[i],dp[i-2][1]]
                elif(dp[i-2][0]+nums[i]<dp[i-1][0]):
                    dp[i]=[dp[i-1][0],dp[i-1][1]]
                else:
                    dp[i]=[dp[i-1][0],min(dp[i-2][1],dp[i-1][1])]
            if(dp[-1][1]==0):
                m=dp[-1][0]
            else:
                m=dp[-2][0]
        nums=nums[1:]
        n-=1
        dp=[[] for i in range(n)]
        dp[0]=[nums[0],1]
        if(nums[0]>nums[1]):
            dp[1]=[nums[0],1]
        else:
            dp[1]=[nums[1],0]
        for i in range(2,n):
            if(dp[i-2][0]+nums[i]>dp[i-1][0]):
                dp[i]=[dp[i-2][0]+nums[i],dp[i-2][1]]
            elif(dp[i-2][0]+nums[i]<dp[i-1][0]):
                dp[i]=[dp[i-1][0],dp[i-1][1]]
            else:
                dp[i]=[dp[i-1][0],min(dp[i-2][1],dp[i-1][1])]
        return max(m,dp[-1][0])
                