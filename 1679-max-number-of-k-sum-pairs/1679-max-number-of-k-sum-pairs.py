class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=0
        l=0
        r=len(nums)-1
        while(l<r):
            if(nums[l]+nums[r]==k):
                ans+=1
                l+=1
                r-=1
            elif(nums[l]+nums[r]>k):
                r-=1
            else:
                l+=1
        return ans