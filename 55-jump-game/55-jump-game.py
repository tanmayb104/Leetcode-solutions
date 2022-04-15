class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp=[False for i in range(len(nums))]
        # dp[0]=True
        m=1
        ma=1
        for i in range(len(nums)):
            # print(m,ma)
            if(m>i):
                m=max(m,ma+nums[i])
                ma+=1
            else:
                return False
        return True
            