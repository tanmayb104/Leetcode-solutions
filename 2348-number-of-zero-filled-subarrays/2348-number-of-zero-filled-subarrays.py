class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        c=0
        for i in range(len(nums)):
            if(nums[i]==0):
                c+=1
            else:
                ans+=(c*(c+1)//2)
                c=0
        ans+=(c*(c+1)//2)
        c=0
        return ans