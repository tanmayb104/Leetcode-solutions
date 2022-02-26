class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        def calc(nums):
            n=len(nums)
            dp=[0 for i in range(n)]
            if(n==1):
                return nums[0]
            elif(n==2):
                return max(nums[0],nums[1])
            else:
                dp[0]=nums[0]
                dp[1]=max(nums[0],nums[1])
                for i in range(2,n):
                    dp[i]=max(dp[i-2]+nums[i],dp[i-1])
                return dp[-1]
        return max(calc(nums[1:]),calc(nums[:-1]))
                