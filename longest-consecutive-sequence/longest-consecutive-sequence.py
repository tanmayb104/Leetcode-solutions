class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(not len(nums)):
            return 0
        ans=1
        nums=list(set(nums))
        nums.sort()
        c=1
        for i in range(1,len(nums)):
            if(nums[i-1]+1==nums[i]):
                c+=1
                ans=max(c,ans)
            else:
                c=1
        return ans