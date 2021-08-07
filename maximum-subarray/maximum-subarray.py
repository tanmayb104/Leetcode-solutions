class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=-99999999999999
        ma=0
        for i in range(len(nums)):
            ma+=nums[i]
            ans=max(ma,ans)
            if(ma<0):
                ma=0
        return ans