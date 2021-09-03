class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        s=0
        ans=999999999999999
        while(r<len(nums)):
            while(s<target and r<len(nums)):
                s+=nums[r]
                r+=1
            while(s>=target):
                ans=min(ans,r-l)
                s-=nums[l]
                l+=1
        if(ans==999999999999999):
            ans=0
        return ans